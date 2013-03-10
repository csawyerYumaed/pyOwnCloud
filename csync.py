#!/usr/bin/env python

import os
import sys
import argparse
import ConfigParser
import ctypes
import re

import csynclib
import version
VERSION = version.version

#Use global variables for user/pass & fingerprint because we have to handle this C callback stuff.
USERNAME = ''
PASSWORD = ''
#TODO, right now, we just blindly accept SSL servers.
SSLFINGERPRINT = ''

def authCallback(prompt, buffer, bufferLength, echo, verify, userData):
	"""
	(const char *prompt, char *buf, size_t len,
		int echo, int verify, void *userdata)
	called like this:
		("Enter your username: ", buf, NE_ABUFSIZ-1, 1, 0, dav_session.userdata )
		type is 1 for username, 0 for password.
	"""
	#print 'authCallback:', prompt,  buffer,  bufferLength, echo, verify, userData
	#print 'string:', ctypes.string_at(buffer, bufferLength-1)
	ret = ''
	if 'username' in prompt:
		ret = USERNAME
	elif 'password' in prompt:
		ret = PASSWORD
	elif 'SSL' in prompt:
		fingerprint = re.search("fingerprint: ([\\w\\d:]+)", prompt).group(1)
		if fingerprint == SSLFINGERPRINT:
			ret = 'yes'
		else:
			print 'SSL fingerpting: %s not accepted, aborting' % fingerprint
			ret = 'no'
	else:
		print 'authCallback: unknown prompt:', prompt
		return -1
	bufferLength = len(ret)
	for i in range(len(ret)):
		ctypes.memset(buffer+i, ord(ret[i]), 1)
	#print 'returning:', ctypes.string_at(buffer, bufferLength)
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
		self.cfg = cfg
		global USERNAME, PASSWORD, SSLFINGERPRINT
		USERNAME = cfg['user']
		PASSWORD = cfg['pass']
		SSLFINGERPRINT = cfg['sslFingerprint']
		c = csynclib.CSYNC()
		self.ctx = ctypes.pointer(c)
		self.buildURL()
		#import pprint
		#pprint.pprint(self.cfg)
		print 'syncing %s to %s logging in as user: %s' %  (self.cfg['src'], 
			self.cfg['url'],
			USERNAME,
			)
		if cfg['dry_run']:
			return
		self.sync()

	def buildURL(self):
		"""build the URL we use for owncloud"""
		url = self.cfg['url']
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



	def sync(self):
		r = csynclib.csync_create(self.ctx, self.cfg['src'], self.cfg['url'])
		if r != 0:
			error(self.ctx,'csync_create', r)
		csynclib.csync_set_log_callback(self.ctx, csynclib.csync_log_callback(log))
		acb = csynclib.csync_auth_callback(authCallback)
		csynclib.csync_set_auth_callback(self.ctx, acb)

		r = csynclib.csync_init(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_init', r)
		#csynclib.csync_set_log_verbosity(ctx, 11)
		r = csynclib.csync_update(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_update', r)
		r = csynclib.csync_reconcile(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_reconcile', r)
		#print 'reconcile done'
		r = csynclib.csync_propagate(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_propogate', r)
		r = csynclib.csync_destroy(self.ctx)
		if r != 0:
			error(self.ctx, 'csync_destroy', r)
		return

def log(ctx, verbosity, function, buffer, userdata):
	"""Log stuff from the ocsync library, but it does not work..."""
	print 'LOG:', verbosity, function, buffer, userdata
	return 0

def error(ctx, cmd, returnCode):
	"""handle library errors"""
	errNum = csynclib.csync_get_error(ctx)
	errMsg = csynclib.csync_get_error_string(ctx)
	print 'ERROR: %s exited %s, error %s: %s' % (
		cmd,
		returnCode,
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
		print 'unkown/not supported platform:', sys.platform
		sys.exit(1)
	return cfgPath

def getConfig(args):
	cfg = {}
	cfgFile = None
	if args['config']:
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
			cfg = dict(c.items('ownCloud'))
	cfg.setdefault('pass', '')
	cfg.setdefault('sslFingerprint', '')
	cfg.setdefault('davPath', 'remote.php/webdav/')

	if os.environ.has_key('OCPASS'):
		cfg['pass'] = os.environ['OCPASS']
	#make sure we take it out if it's None, for environ option.
	if not args['pass']:
		del args['pass']
	#cmd line arguments win out over config files.
	cfg.update(args)
	return cfg

def main(args):
	cfg = getConfig(args)
	sync = ownCloudSync(cfg)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description = 'Synchronize files across machines using ownCloud DAV server',
		epilog = """
I support the ownCloud config file, which is located here:
  {cfg}
I only support the 'ownCloud' section of the config.
I support the following keys in the cfg  file:
	user: The username on the ownCloud server
	url: the url of the ownCloud Server
	pass: the password on the ownCloud server
	sslFingerprint: a valid SSL fingerprint for the server.
	src: local directory to sync against.
	dst: folder on the server to sync against.
complete example:
[ownCloud]
user=awesomeSauce
pass=PasswordThisIsSuperSuperSecretReallyISwearLOL
url=url=https://www.example.org/owncloud/
sslFingerprint=
src=/home/awesomeSauce/ownCloud
dst=clientsync

Password options:
  *) You can specify on the cmd line: -p (not very safe)
  *) in the envifonment variable: OCPASS
  *) in the owncloud.cfg file as pass = <password>
  the choice is yours, if you put it in the cfg file, be careful to 
  make sure nobody but you can read the file. (0400/0600 file perms)
		""".format(cfg = os.path.join(getConfigPath(),'owncloud.cfg')),
	)
	v = "%s - repo: %s" % (VERSION.asString, VERSION.asHead)
	parser.add_argument('-v', '--version', 
		action='version', 
		version = '%(prog)s ' + v)
	parser.add_argument('-c', '--config', nargs='?', default = None,
		help = "username on server.")
	parser.add_argument('-u', '--user', nargs='?', default = None,
		help = "username on server.")
	parser.add_argument('--ssl', nargs='?', default = None,
		dest = 'sslFingerprint',
		help = "SSL fingerprint on server to accept.")
	parser.add_argument('-p', '--pass', nargs='?',
		help = "password on server. you can also store this in environment variable OCPASS")
	parser.add_argument('--dry-run', action = 'store_true', default = False,
		help = "Dry Run, do not actually execute command.")
	parser.add_argument('-s', '--src', nargs='?',
		default =  os.path.expanduser(os.path.join('~','ownCloud')),
		 help = "local Directory to sync with")
	parser.add_argument('-d', '--dst', nargs='?', default = 'clientsync',
		help = "fodler on server.")
	parser.add_argument('--url', nargs='?', default = '',
		 help = "url to sync to.")
	args = vars(parser.parse_args())
	main(args)

