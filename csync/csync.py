#!/usr/bin/env python

import os
import sys
import argparse
import ConfigParser
import ctypes
import re
import pprint
import copy
import getpass

try:
	import keyring
except:
	keyring = None

try:
    from progressbar import ProgressBar, Percentage, Bar, ETA, FileTransferSpeed
except ImportError:
    ProgressBar = None

import csynclib
import version
VERSION = version.version

#Use global variables for user/pass & fingerprint because we have to handle this C callback stuff.
USERNAME = ''
PASSWORD = ''
PASSWORD_SAFE = '********'
SSLFINGERPRINT = ''
DEBUG = False
USE_KEYRING = False

def CSYNC_VERSION_INT(a, b, c):
    return ((a) << 16 | (b) << 8 | (c))

def authCallback(prompt, buffer, bufferLength, echo, verify, userData):
	"""
	(const char *prompt, char *buf, size_t len,
		int echo, int verify, void *userdata)
	called like this:
		("Enter your username: ", buf, NE_ABUFSIZ-1, 1, 0, dav_session.userdata )
		type is 1 for username, 0 for password.
	"""
	if DEBUG:
		print 'authCallback:', prompt,  buffer,  bufferLength, echo, verify, userData
		#print 'string:', ctypes.string_at(buffer, bufferLength-1)
	ret = None
	if 'username' in prompt:
		ret = USERNAME
	elif 'password' in prompt:
		if keyring and USE_KEYRING:
			print "using password from keyring"
			ret = keyring.get_password('ownCloud', USERNAME)
		if ret is None:
			if not PASSWORD:
				ret = getpass.getpass('ownCloud password:')
			else:
				ret = PASSWORD
			if keyring and USE_KEYRING:
				print "saving password to keyring"
				keyring.set_password('ownCloud', USERNAME, ret)
	elif 'SSL' in prompt:
		fingerprint = re.search("fingerprint: ([\\w\\d:]+)", prompt).group(1)
		if fingerprint == SSLFINGERPRINT:
			ret = 'yes'
		else:
			print 'SSL fingerprint: %s not accepted, aborting' % fingerprint
			ret = 'no'
	else:
		print 'authCallback: unknown prompt:', prompt
		return -1
	bufferLength = len(ret)
	for i in range(len(ret)):
		ctypes.memset(buffer+i, ord(ret[i]), 1)
	if DEBUG:
		buffString = ctypes.string_at(buffer, bufferLength)
		if PASSWORD:
			if PASSWORD in buffString:
				buffString = buffString.replace(PASSWORD, PASSWORD_SAFE)
		print 'returning:', buffString
	return 0

class ownCloudSync():
	"""This handles the actual syncying with ownCloud
	cfg is a {}.  should have these things:
		user:
		pass:
		url:
		src:
	None of them are optional. :)
	optional items:
		SSLfingerPrint:
	"""
	def __init__(self, cfg = None):
		"""initialize"""
		self.progress_callback = None
		self.cfg = cfg
		global USERNAME, PASSWORD, SSLFINGERPRINT, USE_KEYRING
		USERNAME = cfg['user']
		PASSWORD = cfg['pass']
		SSLFINGERPRINT = cfg['sslfingerprint']
		USE_KEYRING = cfg['use_keyring']
		libVersion = csynclib.csync_version(0,40,1)
		if DEBUG:
			print 'libocsync version: ', libVersion
		c = csynclib.CSYNC()
		self.ctx = ctypes.pointer(c)
		self.buildURL()
		#pprint.pprint(self.cfg)
		print 'Syncing %s to %s logging in as user: %s' %  (self.cfg['src'], 
			self.cfg['url'],
			USERNAME,
			)
		if cfg.has_key('dry_run') and cfg['dry_run']:
			return
		self.sync()

	def buildURL(self):
		"""build the URL we use for owncloud"""
		url = self.cfg['url']
		if not url:
			print 'You must specify a url, use --url, or put in cfg file.'
			sys.exit(1)
		url = url.replace('https','ownclouds')
		url = url.replace('http','owncloud')
		#add / if needed
		if url[-1:] != '/':
			url = ''.join((url,'/'))
		url += self.cfg['davPath']
		#add / if needed
		if url[-1:] != '/':
			url = ''.join((url,'/'))
		url = ''.join((url, self.cfg['dst']))
		#take off any trailing slash.
		if url[-1:] == '/':
			url = url[:-1]
		self.cfg['url'] = url
		if DEBUG:
			print 'buildURL: ', url
		return

	def sync(self):
		r = csynclib.csync_create(self.ctx, self.cfg['src'], self.cfg['url'])
		if r != 0:
			error(self.ctx,'csync_create', r)
		csynclib.csync_set_log_callback(self.ctx, csynclib.csync_log_callback(log))
		acb = csynclib.csync_auth_callback(authCallback)
		if DEBUG:
			print 'authCallback setup'
		csynclib.csync_set_auth_callback(self.ctx, acb)

		if self.cfg['progress']:
			csynclib.csync_set_progress_callback(self.ctx, self.get_progress_callback())

		r = csynclib.csync_init(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_init', r)
		if DEBUG:
			print 'Initialization done.'
		if self.cfg.has_key('usedownloadlimit') or self.cfg.has_key('useuploadlimit'):
			if csynclib.csync_version(CSYNC_VERSION_INT(0,81,0)) is None:
				print 'Bandwidth throttling requires ocsync version >= 0.81.0, ignoring limits'
			else:
				if self.cfg.has_key('usedownloadlimit') and self.cfg['usedownloadlimit'] and self.cfg.has_key('downloadlimit'):
					dlimit = ctypes.c_int(int(self.cfg['downloadlimit']) * 1000)
					if DEBUG:
						print 'Download limit: ', dlimit.value
					csynclib.csync_set_module_property(self.ctx, 'bandwidth_limit_download', ctypes.pointer(dlimit))
				if self.cfg.has_key('useuploadlimit') and self.cfg['useuploadlimit'] and self.cfg.has_key('uploadlimit'):
					ulimit = ctypes.c_int(int(self.cfg['uploadlimit']) * 1000)
					if DEBUG:
						print 'Upload limit: ', ulimit.value
					csynclib.csync_set_module_property(self.ctx,'bandwidth_limit_upload',ctypes.pointer(ulimit))
		#csynclib.csync_set_log_verbosity(self.ctx, ctypes.c_int(11))
		r = csynclib.csync_update(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_update', r)
		if DEBUG:
			print 'Update done.'
		r = csynclib.csync_reconcile(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_reconcile', r)
		if DEBUG:
			print 'Reconcile done.'
		r = csynclib.csync_propagate(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_propogate', r)
		if DEBUG:
			print 'Propogate finished, destroying.'
		r = csynclib.csync_destroy(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_destroy', r)

	def get_progress_callback(self):
		def progress_wrapper(progress_p, userdata_p):
			if progress_p:
				progress_p = progress_p[0]
			if userdata_p:
				userdata_p = userdata_p[0]
			return self.progress(progress_p, userdata_p)
		if not self.progress_callback:
			self.progress_callback = csynclib.csync_progress_callback(progress_wrapper)
		return self.progress_callback

	def progress(self, progress, userdata):
		progress_text = {
			csynclib.CSYNC_NOTIFY_INVALID: "invalid",
			csynclib.CSYNC_NOTIFY_START_SYNC_SEQUENCE: "start syncing",
			csynclib.CSYNC_NOTIFY_START_DOWNLOAD: "start downloading",
			csynclib.CSYNC_NOTIFY_START_UPLOAD: "start uploading",
			csynclib.CSYNC_NOTIFY_PROGRESS: "progess message",
			csynclib.CSYNC_NOTIFY_FINISHED_DOWNLOAD: "finished downloading",
			csynclib.CSYNC_NOTIFY_FINISHED_UPLOAD: "finished uploading",
			csynclib.CSYNC_NOTIFY_FINISHED_SYNC_SEQUENCE: "finished sycing",
			csynclib.CSYNC_NOTIFY_START_DELETE: "start deleted",
			csynclib.CSYNC_NOTIFY_END_DELETE: "end deleted",
			csynclib.CSYNC_NOTIFY_ERROR: "error",
			}

		if progress.kind in (csynclib.CSYNC_NOTIFY_START_UPLOAD, csynclib.CSYNC_NOTIFY_START_DOWNLOAD, csynclib.CSYNC_NOTIFY_START_DELETE):
			maxval = progress.overall_file_count
			if progress.kind == csynclib.CSYNC_NOTIFY_START_UPLOAD:
				self.progress_mode = "Uploading "
			if progress.kind == csynclib.CSYNC_NOTIFY_START_DOWNLOAD:
				self.progress_mode = "Downloading "
			if progress.kind == csynclib.CSYNC_NOTIFY_START_DELETE:
				self.progress_mode = "Deleting "
				maxval = progress.overall_transmission_size

			fname = progress.path[len(self.cfg['url'])+1:]
			widgets = [self.progress_mode, fname, ' ', Percentage(), ' ', Bar(),
				' ', ETA(), ' ', FileTransferSpeed()]
			self.pbar = ProgressBar(widgets=widgets, maxval=maxval).start()
		elif progress.kind in (csynclib.CSYNC_NOTIFY_FINISHED_DOWNLOAD, csynclib.CSYNC_NOTIFY_FINISHED_UPLOAD, csynclib.CSYNC_NOTIFY_END_DELETE):
			self.pbar.finish()
			return
		elif progress.kind == csynclib.CSYNC_NOTIFY_PROGRESS:
			self.pbar.update(progress.curr_bytes)
		else:
			if progress.kind in (csynclib.CSYNC_NOTIFY_START_SYNC_SEQUENCE, csynclib.CSYNC_NOTIFY_FINISHED_SYNC_SEQUENCE):
				return
			print progress_text[progress.kind]
			print progress.path, progress.file_size, progress.curr_bytes, progress.overall_file_count, progress.current_file_no, progress.overall_transmission_size, progress.current_overall_bytes

def log(ctx, verbosity, function, buffer, userdata):
	"""Log stuff from the ocsync library, but it does not work..."""
	print 'LOG:', verbosity, function, buffer, userdata
	return 0

def error(ctx, cmd, returnCode):
	"""handle library errors"""
	libVersion = csynclib.csync_version(0,40,1)
	errNum = csynclib.csync_get_error(ctx)
	errMsg = csynclib.csync_get_error_string(ctx)
	if not errMsg:
		if errNum == csynclib.CSYNC_ERR_AUTH_SERVER and cmd == 'csync_update':
			errMsg = 'This is an authentication problem with the server, check user/pass.'
		if errNum == csynclib.CSYNC_ERR_NOT_FOUND and cmd == 'csync_update':
			errMsg = 'This is a remote folder destination issue, check that the remote folder exists on ownCloud.'
	print 'ERROR: %s exited with %s, csync(%s) error %s: %s' % (
		cmd,
		returnCode,
		libVersion,
		errNum,
		errMsg,
		)
	sys.exit(1)

def getConfigPath():
	"""get the local configuration file path
	"""
	if sys.platform.startswith('linux'):
		cfgPath = os.path.join('~','.local','share','data','ownCloud')
		cfgPath = os.path.expanduser(cfgPath) 
	elif sys.platform == 'darwin':
		cfgPath = os.path.join('~','Library','Application Support','ownCloud')
		cfgPath = os.path.expanduser(cfgPath) 
	elif 'win' in sys.platform:
		cfgPath = os.path.join('%LOCALAPPDATA%','ownCloud')
		cfgPath = os.path.expandvars(cfgPath)
	else:
		print 'Unkown/not supported platform %s, please file a bug report. ' % sys.platform
		sys.exit(1)
	if DEBUG:
		print 'getConfigPath:', cfgPath
	return cfgPath

def getConfig(parser):
	args = vars(parser.parse_args())
	if DEBUG:
		print 'From args: '
		pargs = copy.copy(args)
		if pargs['pass']:
			pargs['pass'] = PASSWORD_SAFE
		pprint.pprint(pargs)
	newArgs = {}
	for k, v in args.iteritems():
		if v:
			newArgs[k] = v
	args = newArgs
	cfg = {}
	cfgFile = None
	if args.has_key('config'):
		cfgFile = args['config']
	else:
		cfgPath = getConfigPath()
		if os.path.exists(os.path.join(cfgPath,'owncloud.cfg')):
			cfgFile = os.path.join(cfgPath, 'owncloud.cfg')
	if cfgFile:
		with open(cfgFile) as fd:
			"""We use the INI file format that Mirall does. we allow more
			things in the cfg file...
				pass: the password
			"""
			c = ConfigParser.SafeConfigParser()
			c.readfp(fd)
			if csynclib.csync_version(CSYNC_VERSION_INT(0,81,0)) is None:
				cfg = dict(c.items('ownCloud'))
			else:
				if c.has_section('BWLimit'):
					cfg = dict(c.items('BWLimit') + c.items('ownCloud'))
				else:
					if DEBUG:
						print 'config file has no section [BWLimit]'
					cfg = dict(c.items('ownCloud'))
			if DEBUG:
				print 'conifguration info received from %s:' % cfgFile
				pcfg = copy.copy(cfg)
				if pcfg.has_key('pass'):
					pcfg['pass'] = PASSWORD_SAFE
				pprint.pprint(pcfg)
	cfg.setdefault('davPath', 'remote.php/webdav/')
	cfg.setdefault('sslfingerprint' '')
	cfg.setdefault('pass', None)
	cfg.setdefault('user', getpass.getuser())
	cfg.setdefault('use_keyring', False)
	cfg.setdefault('progress', False)
	if os.environ.has_key('OCPASS'):
		cfg['pass'] = os.environ['OCPASS']
		if DEBUG:
			print 'password coming from environment'
	#cmd line arguments win out over config files.
	parser.set_defaults(**cfg)
	args = vars(parser.parse_args())
	cfg.update(args)
	if DEBUG:
		print 'Finished config file:'
		pcfg = copy.copy(cfg)
		if pcfg.has_key('pass'):
			pcfg['pass'] = PASSWORD_SAFE
		pprint.pprint(pcfg)
	return cfg

def startSync(parser):
	cfg = getConfig(parser)
	try:
		ownCloudSync(cfg)
	except KeyError:
		exc_type, exc_value, exc_tb = sys.exc_info()
		print 'Sorry this option: %s is required, was not found in cfg file or on cmd line.' % (exc_value)
		if DEBUG:
			raise

def main():
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description = 'Synchronize files across machines using ownCloud DAV server.',
		epilog = """
oclient supports the ownCloud config file, which is located here:
  {cfg}
oclient only supports the 'ownCloud' section of the config.
oclient supports the following keys in the cfg  file:
    user: username on the ownCloud server
	pass: password on the ownCloud server
	url: url of the ownCloud server
	sslfingerprint: valid SSL fingerprint for the server
	src: local directory to sync against
	dst: folder on the server to sync against
complete example:
[ownCloud]
user=awesomeSauce
pass=PasswordThisIsSuperSuperSecretReallyISwearLOL
url=https://www.example.org/owncloud/
sslfingerprint=
src=/home/awesomeSauce/ownCloud
dst=clientsync

Password options:
  *) You can specify on the cmd line: -p (not very safe)
  *) In the envifonment variable: OCPASS
  *) In the owncloud.cfg file as pass = <password>
  *) Do none of the above, and it will prompt you for the password.
  *) Use keyring to store passwords in a keyring. (keyring package is {keyring}installed)
  The choice is yours, if you put it in the cfg file, be careful to
  make sure nobody but you can read the file. (0400/0600 file perms).
		""".format(cfg = os.path.join(getConfigPath(),'owncloud.cfg'), keyring="" if keyring else "NOT "),
	)
	v = "%s - repo: %s" % (VERSION.asString, VERSION.asHead)
	parser.add_argument('-v', '--version', 
		action='version', 
		version = '%(prog)s ' + v)
	parser.add_argument('-c', '--config', nargs='?', default = None,
		help = "Configuration to use.")
	parser.add_argument('-u', '--user', nargs='?', default = None,
		help = "Username on server.")
	parser.add_argument('--ssl', nargs='?', default = None,
		dest = 'sslfingerprint',
		help = "SSL fingerprint on server to accept.")
	parser.add_argument('-p', '--pass', nargs='?', default = None,
		help = "Password on server. You can also store this in environment variable OCPASS.")
	parser.add_argument('--dry-run', action = 'store_true', default = False,
		help = "Dry Run, do not actually execute command.")
	parser.add_argument('--debug', action = 'store_true', default = False,
		help = "Print a bunch of debug info.")
	parser.add_argument('-s', '--src', nargs='?',
		default =  os.path.expanduser(os.path.join('~','ownCloud')),
		help = "Local Directory to sync with.")
	parser.add_argument('-d', '--dst', nargs='?', default = 'clientsync',
		help = "Folder on server.")
	parser.add_argument('--url', nargs='?', default = None,
		help = "URL to sync to.")
	if csynclib.csync_version(CSYNC_VERSION_INT(0,81,0)) is not None:
		parser.add_argument('--usedownloadlimit', action = 'store_true', default = None,
			help = "Use download limit.")
		parser.add_argument('--useuploadlimit', action = 'store_true', default = None,
			help = "Use upload limit.")
		parser.add_argument('--downloadlimit', nargs = '?', default = 0,
			help = "Download limit in KB/s.")
		parser.add_argument('--uploadlimit', nargs = '?', default = 0,
			help = "Upload limit in KB/s.")
	if keyring:
		parser.add_argument('--use-keyring', action = 'store_true', default = False,
				help = "use keyring if available to store password safely.")
	if ProgressBar and csynclib.csync_version(CSYNC_VERSION_INT(0,90,0)) is not None:
		parser.add_argument('--progress', action = 'store_true', default = False,
				help = "show progress while syncing.")
	args = vars(parser.parse_args())
	if args['debug']:
		global DEBUG
		DEBUG = True
		print 'Turning debug on'
	startSync(parser)

if __name__ == '__main__':
	import signal
	def signal_handler(signal, frame):
		print '\nYou pressed Ctrl+C'
		sys.exit(1)
	signal.signal(signal.SIGINT, signal_handler)
	main()

# vim: noet:ts=4:sw=4:sts=4
