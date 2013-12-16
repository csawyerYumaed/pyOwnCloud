import sys
import os.path
import ctypes.util
import logging
from ctypes import CDLL
from ctypes import c_char_p, c_int

def getCSync():
    logger = logging.getLogger(__name__)
	if os.path.exists('/usr/lib/libocsync.so.0'):
        logger.debug('Found ocsync at %s', '/usr/lib/libocsync.so.0')
		return CDLL('/usr/lib/libocsync.so.0')
	elif os.path.exists('/usr/lib64/libocsync.so.0'):
        logger.debug('Found ocsync at %s', '/usr/lib64/libocsync.so.0')
		return CDLL('/usr/lib64/libocsync.so.0')
	else:
		path = ctypes.util.find_library('ocsync')
		if path:
            logger.debug('Found ocsync at %s', path)
			return CDLL(path)
    logger.critical('Could not find shared library libocsync')
    sys.exit(1)


csynclib = getCSync()

csync_version = csynclib.csync_version
csync_version.restype = c_char_p
csync_version.argtypes = [c_int]

__all__ = ['getCSync','csynclib','csync_version']

# vim: noet:ts=4:sw=4:sts=4
