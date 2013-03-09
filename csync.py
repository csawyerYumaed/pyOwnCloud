#!/usr/bin/env python

import sys

import csynclib
import ctypes

def getUser():
	"""return the username for authentication to the ownCloud server"""
	return 'USER'

def getPass():
	"""return the password for authentication to the ownCloud server"""
	return 'password'

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

def authCallback(prompt, buffer, bufferLength, echo, verify, userData):
	"""
	(const char *prompt, char *buf, size_t len,
	    int echo, int verify, void *userdata)
	called like this:
		("Enter your username: ", buf, NE_ABUFSIZ-1, 1, 0, dav_session.userdata )
		type is 1 for username, 0 for password.
	"""
	print 'authCallback:', prompt,  buffer,  bufferLength, echo, verify, userData
	#print 'string:', ctypes.string_at(buffer, bufferLength-1)
	ret = ''
	if 'username' in prompt:
		ret = getUser()
	elif 'password' in prompt:
		ret = getPass()
	elif 'SSL' in prompt:
		ret = 'yes'
	else:
		print 'authCallback: unknown prompt:', prompt
		return -1
	bufferLength = len(ret)
	for i in range(len(ret)):
		ctypes.memset(buffer+i, ord(ret[i]), 1)
	#print 'returning:', ctypes.string_at(buffer, bufferLength)
	return 0

def sync(local, remote):
	c = csynclib.CSYNC()
	ctx = ctypes.pointer(c)
	r = csynclib.csync_create(ctx, local, remote)
	if r != 0:
		error(ctx,'csync_create', r)
	csynclib.csync_set_log_callback(ctx, csynclib.csync_log_callback(log))
	acb = csynclib.csync_auth_callback(authCallback)
	csynclib.csync_set_auth_callback(ctx, acb)
	r = csynclib.csync_init(ctx)
	if r != 0:
		error(ctx, 'csync_init', r)
	#csynclib.csync_set_log_verbosity(ctx, 11)
	r = csynclib.csync_update(ctx)
	if r != 0:
		error(ctx, 'csync_update', r)
	r = csynclib.csync_reconcile(ctx)
	if r != 0:
		error(ctx, 'csync_reconcile', r)
	print 'reconcile done'
	r = csynclib.csync_propagate(ctx)
	if r != 0:
		error(ctx, 'csync_propogate', r)
	r = csynclib.csync_destroy(ctx)
	if r != 0:
		error(ctx, 'csync_destroy', r)
	return 

def main(src, dst):
	sync(src,dst)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
