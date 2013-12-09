import os.path
import ctypes.util
from ctypes import CDLL
from ctypes import c_char_p, c_int

def getCSync():
	if os.path.exists('/usr/lib/libocsync.so.0'):
		return CDLL('/usr/lib/libocsync.so.0')
	elif os.path.exists('/usr/lib64/libocsync.so.0'):
		return CDLL('/usr/lib64/libocsync.so.0')
	else:
		path = ctypes.util.find_library('ocsync')
		if path:
			return CDLL(path)
	raise('Could not find shared library libocsync')


csynclib = getCSync()

csync_version = csynclib.csync_version
csync_version.restype = c_char_p
csync_version.argtypes = [c_int]

__all__ = ['getCSync','csynclib','csync_version']
