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
import logging

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

logging.basicConfig(level=logging.DEBUG, format='%(name)s-%(levelname)s: %(message)s')

#Global variables
VERSION = version.version
PASSWORD_SAFE = '********'
DEBUG = False

def CSYNC_VERSION_INT(a, b, c):
    return ((a) << 16 | (b) << 8 | (c))

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
		self.auth_callback = None
		self.log_callback = None
		self.progress_callback = None
		self.logger = logging.getLogger("pyOC")
		self.cfg = cfg
		self.debug = cfg['debug']
		self._user = cfg['user']
		self._password = cfg['pass']
		self._fingerprint = cfg['sslfingerprint']
		self._keyring = cfg['use_keyring']
		self.libVersion = csynclib.csync_version(0,40,1)
		self.logger.debug('libocsync version: %s', self.libVersion)
		c = csynclib.CSYNC()
		self.ctx = ctypes.pointer(c)
		self.buildURL()
		self.logger.info('Syncing %s to %s logging in as user: %s' , self.cfg['src'],
			self.cfg['url'],
			self._user,
			)
		if cfg.has_key('dry_run') and cfg['dry_run']:
			return
		self.sync()

	def buildURL(self):
		"""build the URL we use for owncloud"""
		url = self.cfg['url']
		if not url:
			self.logger.error('You must specify a url, use --url, or put in cfg file.')
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
		self.logger.debug('buildURL: %s', url)
		return

	def get_auth_callback(self):
		"""gives back the auth callback:
			The actual function is called out of the ownCloudSync object."""
		def auth_wrapper(prompt, buffer, bufferLength, echo, verify, userData):
			return self.authCallback(prompt, buffer, bufferLength, echo, verify, userData)
		if not self.auth_callback:
			self.auth_callback = csynclib.csync_auth_callback(auth_wrapper)
		return self.auth_callback

	def authCallback(self, prompt, buffer, bufferLength, echo, verify, userData):
		"""
		(const char *prompt, char *buf, size_t len,
			int echo, int verify, void *userdata)
		called like this:
			("Enter your username: ", buf, NE_ABUFSIZ-1, 1, 0, dav_session.userdata )
			type is 1 for username, 0 for password.
		calls functions username(), password() or ssl(fingerprint)
		"""
		self.logger.debug("authCallback: '%s', %s, %i, %i, %i, %s", prompt,  buffer,  bufferLength, echo, verify, userData)
		ret = None
		if 'username' in prompt:
			ret = self.username()
		elif 'password' in prompt:
			ret = self.password()
		elif 'SSL' in prompt:
			fingerprint = re.search("fingerprint: ([\\w\\d:]+)", prompt).group(1)
			ret = self.ssl(fingerprint)
		else:
			self.logger.warning("authCallback: unknown prompt: '%s'", prompt)
			return -1
		
		for i in range(len(ret)):
			ctypes.memset(buffer+i, ord(ret[i]), 1)
		if self.debug:
			buffString = ctypes.string_at(buffer, len(ret))
			if 'password' in prompt:
				if ret and ret in buffString:
					buffString = buffString.replace(ret, PASSWORD_SAFE)
			self.logger.debug("returning: '%s'", buffString)
		return 0



	def sync(self):
		r = csynclib.csync_create(self.ctx, self.cfg['src'], self.cfg['url'])
		if r != 0:
			self.error('csync_create', r)
		
		csynclib.csync_set_log_callback(self.ctx, self.get_log_callback())
		csynclib.csync_set_log_verbosity(self.ctx, self.cfg['verbosity_ocsync'])

		self.logger.debug('authCallback setup')
		csynclib.csync_set_auth_callback(self.ctx, self.get_auth_callback())

		if self.cfg['progress']:
			csynclib.csync_set_progress_callback(self.ctx, self.get_progress_callback())
		
		r = csynclib.csync_init(self.ctx)
		if r != 0:
			self.error('csync_init', r)
		self.logger.debug('Initialization done.')
		if (self.cfg.has_key('downloadlimit') and self.cfg['downloadlimit']) or \
			(self.cfg.has_key('uploadlimit') and self.cfg['uploadlimit']):
			if csynclib.csync_version(CSYNC_VERSION_INT(0,81,0)) is None:
				self.logger.warning('Bandwidth throttling requires ocsync version >= 0.81.0, ignoring limits')
			else:
				if self.cfg.has_key('downloadlimit') and self.cfg['downloadlimit']:
					dlimit = ctypes.c_int(int(self.cfg['downloadlimit']) * 1000)
					self.logger.debug('Download limit: %i', dlimit.value)
					csynclib.csync_set_module_property(self.ctx, 'bandwidth_limit_download', ctypes.pointer(dlimit))
				if self.cfg.has_key('uploadlimit') and self.cfg['uploadlimit']:
					ulimit = ctypes.c_int(int(self.cfg['uploadlimit']) * 1000)
					self.logger.debug('Upload limit: %i', ulimit.value)
					csynclib.csync_set_module_property(self.ctx,'bandwidth_limit_upload',ctypes.pointer(ulimit))
		r = csynclib.csync_update(self.ctx)
		if r != 0:
			self.error('csync_update', r)
		self.logger.debug('Update done.')
		r = csynclib.csync_reconcile(self.ctx)
		if r != 0:
			self.error('csync_reconcile', r)
		self.logger.debug('Reconcile done.')
		r = csynclib.csync_propagate(self.ctx)
		if r != 0:
			self.error('csync_propogate', r)
		self.logger.debug('Propogate finished, destroying.')
		r = csynclib.csync_destroy(self.ctx)
		if r != 0:
			self.error('csync_destroy', r)

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
			self.logger.debug(progress_text[progress.kind])
			self.logger.debug("'%s', %i, %i, %i, %i, %i, %i", progress.path, progress.file_size, progress.curr_bytes, progress.overall_file_count, progress.current_file_no, progress.overall_transmission_size, progress.current_overall_bytes)

	def username(self):
		"""returns the username"""
		return self._user

	def password(self):
		"""returns the password"""
		ret = None
		if keyring and self._keyring:
			self.logger.debug("using password from keyring")
			ret = keyring.get_password('ownCloud', self.username())
		if ret is None:
			if not self._password:
				ret = getpass.getpass('ownCloud password:')
			else:
				ret = self._password
			if keyring and self._keyring:
				self.logger.debug("saving password to keyring")
				keyring.set_password('ownCloud', self.username(), ret)
		return ret

	def ssl(self, fingerprint):
		"""returns if fingerprint is valid (yes or no as string)"""
		if fingerprint == self._fingerprint:
			return 'yes'
		else:
			self.logger.error('SSL fingerprint: %s not accepted, aborting' , fingerprint)
			return 'no'


	def get_log_callback(self):
		def log_wrapper(ctx, verbosity, function, buffer, userdata):
			return self.log(verbosity, function, buffer, userdata)
		if not self.log_callback:
			self.log_callback = csynclib.csync_log_callback(log_wrapper)
		return self.log_callback

	def log(self, verbosity, function, buffer, userdata):
		"""Log stuff from the ocsync library."""
		v2l = {csynclib.CSYNC_LOG_PRIORITY_NOLOG: logging.CRITICAL,
			csynclib.CSYNC_LOG_PRIORITY_FATAL: logging.CRITICAL,
			csynclib.CSYNC_LOG_PRIORITY_ALERT: logging.CRITICAL,
			csynclib.CSYNC_LOG_PRIORITY_CRIT: logging.CRITICAL,
			csynclib.CSYNC_LOG_PRIORITY_ERROR: logging.ERROR,
			csynclib.CSYNC_LOG_PRIORITY_WARN: logging.WARN,
			csynclib.CSYNC_LOG_PRIORITY_NOTICE: logging.INFO,
			csynclib.CSYNC_LOG_PRIORITY_INFO: logging.INFO,
			csynclib.CSYNC_LOG_PRIORITY_DEBUG: logging.DEBUG,
			csynclib.CSYNC_LOG_PRIORITY_TRACE: logging.DEBUG,
			csynclib.CSYNC_LOG_PRIORITY_NOTSET: logging.DEBUG,
			csynclib.CSYNC_LOG_PRIORITY_UNKNOWN: logging.DEBUG,
			}

		level = logging.DEBUG
		if verbosity in v2l:
			level = v2l[verbosity]

		logging.getLogger("ocsync").log(level, buffer)

	def error(self, cmd, returnCode):
		"""handle library errors"""
		errNum = csynclib.csync_get_error(self.ctx)
		errMsg = csynclib.csync_get_error_string(self.ctx)
		if not errMsg:
			if errNum == csynclib.CSYNC_ERR_AUTH_SERVER and cmd == 'csync_update':
				errMsg = 'This is an authentication problem with the server, check user/pass.'
			if errNum == csynclib.CSYNC_ERR_NOT_FOUND and cmd == 'csync_update':
				errMsg = 'This is a remote folder destination issue, check that the remote folder exists on ownCloud.'
		self.logger.error('%s exited with %s, csync(%s) error %s: %s',
			cmd,
			returnCode,
			self.libVersion,
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
		logging.warning('Unkown/not supported platform %s, please file a bug report. ', sys.platform)
		sys.exit(1)
	logging.debug('getConfigPath: %s', cfgPath)
	return cfgPath

def getConfig(parser):
	args = vars(parser.parse_args())
	if DEBUG:
		logging.debug('From args: ')
		pargs = copy.copy(args)
		if pargs['pass']:
			pargs['pass'] = PASSWORD_SAFE
		logging.debug(pprint.pformat(pargs))
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
					if not cfg['useuploadlimit']:
						cfg['uploadlimit'] = None
					if not cfg['usedownloadlimit']:
						cfg['downloadlimit'] = None
				else:
					logging.debug('config file has no section [BWLimit]')
					cfg = dict(c.items('ownCloud'))
			if DEBUG:
				logging.debug('configuration info received from %s:', cfgFile)
				pcfg = copy.copy(cfg)
				if pcfg.has_key('pass'):
					pcfg['pass'] = PASSWORD_SAFE
				logging.debug(pprint.pformat(pcfg))
	cfg.setdefault('davPath', 'remote.php/webdav/')
	cfg.setdefault('sslfingerprint' '')
	cfg.setdefault('pass', None)
	cfg.setdefault('user', getpass.getuser())
	cfg.setdefault('use_keyring', False)
	cfg.setdefault('progress', False)
	if os.environ.has_key('OCPASS'):
		cfg['pass'] = os.environ['OCPASS']
		logging.debug('password coming from environment')
	#cmd line arguments win out over config files.
	parser.set_defaults(**cfg)
	args = vars(parser.parse_args())
	cfg.update(args)
	if DEBUG:
		logging.debug('Finished config file:')
		pcfg = copy.copy(cfg)
		if pcfg.has_key('pass'):
			pcfg['pass'] = PASSWORD_SAFE
		logging.debug(pprint.pformat(pcfg))
	return cfg

def startSync(parser):
	cfg = getConfig(parser)
	try:
		ownCloudSync(cfg)
	except KeyError:
		exc_type, exc_value, exc_tb = sys.exc_info()
		logging.error('Sorry this option: %s is required, was not found in cfg file or on cmd line.', exc_value)
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
	parser.add_argument('--verbosity-ocsync', default = csynclib.CSYNC_LOG_PRIORITY_WARN, type=int,
		help = "Verbosity for libocsync. (0=NOLOG,11=Everything)")
	parser.add_argument('-s', '--src', nargs='?',
		default =  os.path.expanduser(os.path.join('~','ownCloud')),
		help = "Local Directory to sync with.")
	parser.add_argument('-d', '--dst', nargs='?', default = 'clientsync',
		help = "Folder on server.")
	parser.add_argument('--url', nargs='?', default = None,
		help = "URL to sync to.")
	if csynclib.csync_version(CSYNC_VERSION_INT(0,81,0)) is not None:
		parser.add_argument('--downloadlimit', nargs = '?', default = None,
			help = "Download limit in KB/s.")
		parser.add_argument('--uploadlimit', nargs = '?', default = None,
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
		logging.debug('Turning debug on')
	else:
		logging.getLogger('').setLevel(logging.INFO)
	startSync(parser)

if __name__ == '__main__':
	import signal
	def signal_handler(signal, frame):
		logging.info('\nYou pressed Ctrl+C')
		sys.exit(1)
	signal.signal(signal.SIGINT, signal_handler)
	main()

# vim: noet:ts=4:sw=4:sts=4
