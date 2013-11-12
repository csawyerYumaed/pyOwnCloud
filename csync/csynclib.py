from ctypes import *
import ctypes.util
import os
import sys

STRING = c_char_p
_libraries = {}
if os.path.exists('/usr/lib/libocsync.so.0'):
	_libraries['/usr/lib/libocsync.so.0'] = CDLL('/usr/lib/libocsync.so.0')
elif os.path.exists('/usr/lib64/libocsync.so.0'):
	_libraries['/usr/lib/libocsync.so.0'] = CDLL('/usr/lib64/libocsync.so.0')
else:
	path = ctypes.util.find_library('ocsync')
	if path:
		print 'Found libocsync @', path
		_libraries['/usr/lib/libocsync.so.0'] = CDLL(path)
	else:
		print 'ERROR, can not find shared library libocsync'
		sys.exit(1)

class LP_LP_csync_s(Structure):
	pass

class csync_s(Structure):
    pass
CSYNC = csync_s
csync_create = _libraries['/usr/lib/libocsync.so.0'].csync_create
csync_create.restype = c_int
csync_create.argtypes = [POINTER(POINTER(CSYNC)), STRING, STRING]
csync_init = _libraries['/usr/lib/libocsync.so.0'].csync_init
csync_init.restype = c_int
csync_init.argtypes = [POINTER(CSYNC)]
csync_update = _libraries['/usr/lib/libocsync.so.0'].csync_update
csync_update.restype = c_int
csync_update.argtypes = [POINTER(CSYNC)]
csync_reconcile = _libraries['/usr/lib/libocsync.so.0'].csync_reconcile
csync_reconcile.restype = c_int
csync_reconcile.argtypes = [POINTER(CSYNC)]
csync_propagate = _libraries['/usr/lib/libocsync.so.0'].csync_propagate
csync_propagate.restype = c_int
csync_propagate.argtypes = [POINTER(CSYNC)]
csync_destroy = _libraries['/usr/lib/libocsync.so.0'].csync_destroy
csync_destroy.restype = c_int
csync_destroy.argtypes = [POINTER(CSYNC)]
csync_version = _libraries['/usr/lib/libocsync.so.0'].csync_version
csync_version.restype = STRING
csync_version.argtypes = [c_int]
csync_add_exclude_list = _libraries['/usr/lib/libocsync.so.0'].csync_add_exclude_list
csync_add_exclude_list.restype = c_int
csync_add_exclude_list.argtypes = [POINTER(CSYNC), STRING]
csync_get_config_dir = _libraries['/usr/lib/libocsync.so.0'].csync_get_config_dir
csync_get_config_dir.restype = STRING
csync_get_config_dir.argtypes = [POINTER(CSYNC)]
csync_set_config_dir = _libraries['/usr/lib/libocsync.so.0'].csync_set_config_dir
csync_set_config_dir.restype = c_int
csync_set_config_dir.argtypes = [POINTER(CSYNC), STRING]
csync_enable_statedb = _libraries['/usr/lib/libocsync.so.0'].csync_enable_statedb
csync_enable_statedb.restype = c_int
csync_enable_statedb.argtypes = [POINTER(CSYNC)]
csync_disable_statedb = _libraries['/usr/lib/libocsync.so.0'].csync_disable_statedb
csync_disable_statedb.restype = c_int
csync_disable_statedb.argtypes = [POINTER(CSYNC)]
csync_is_statedb_disabled = _libraries['/usr/lib/libocsync.so.0'].csync_is_statedb_disabled
csync_is_statedb_disabled.restype = c_int
csync_is_statedb_disabled.argtypes = [POINTER(CSYNC)]
csync_get_userdata = _libraries['/usr/lib/libocsync.so.0'].csync_get_userdata
csync_get_userdata.restype = c_void_p
csync_get_userdata.argtypes = [POINTER(CSYNC)]
csync_set_userdata = _libraries['/usr/lib/libocsync.so.0'].csync_set_userdata
csync_set_userdata.restype = c_int
csync_set_userdata.argtypes = [POINTER(CSYNC), c_void_p]
size_t = c_ulong
csync_auth_callback = CFUNCTYPE(c_int, STRING, c_void_p, size_t, c_int, c_int, c_void_p)
csync_get_auth_callback = _libraries['/usr/lib/libocsync.so.0'].csync_get_auth_callback
csync_get_auth_callback.restype = csync_auth_callback
csync_get_auth_callback.argtypes = [POINTER(CSYNC)]
csync_set_auth_callback = _libraries['/usr/lib/libocsync.so.0'].csync_set_auth_callback
csync_set_auth_callback.restype = c_int
csync_set_auth_callback.argtypes = [POINTER(CSYNC), csync_auth_callback]
csync_set_log_verbosity = _libraries['/usr/lib/libocsync.so.0'].csync_set_log_verbosity
csync_set_log_verbosity.restype = c_int
csync_set_log_verbosity.argtypes = [POINTER(CSYNC), c_int]
csync_get_log_verbosity = _libraries['/usr/lib/libocsync.so.0'].csync_get_log_verbosity
csync_get_log_verbosity.restype = c_int
csync_get_log_verbosity.argtypes = [POINTER(CSYNC)]
csync_log_callback = CFUNCTYPE(None, POINTER(CSYNC), c_int, STRING, STRING, c_void_p)
csync_get_log_callback = _libraries['/usr/lib/libocsync.so.0'].csync_get_log_callback
csync_get_log_callback.restype = csync_log_callback
csync_get_log_callback.argtypes = [POINTER(CSYNC)]
csync_set_log_callback = _libraries['/usr/lib/libocsync.so.0'].csync_set_log_callback
csync_set_log_callback.restype = c_int
csync_set_log_callback.argtypes = [POINTER(CSYNC), csync_log_callback]
csync_get_statedb_file = _libraries['/usr/lib/libocsync.so.0'].csync_get_statedb_file
csync_get_statedb_file.restype = STRING
csync_get_statedb_file.argtypes = [POINTER(CSYNC)]
csync_enable_conflictcopys = _libraries['/usr/lib/libocsync.so.0'].csync_enable_conflictcopys
csync_enable_conflictcopys.restype = c_int
csync_enable_conflictcopys.argtypes = [POINTER(CSYNC)]
csync_set_local_only = _libraries['/usr/lib/libocsync.so.0'].csync_set_local_only
csync_set_local_only.restype = c_int
csync_set_local_only.argtypes = [POINTER(CSYNC), c_bool]
csync_get_local_only = _libraries['/usr/lib/libocsync.so.0'].csync_get_local_only
csync_get_local_only.restype = c_bool
csync_get_local_only.argtypes = [POINTER(CSYNC)]
csync_get_status = _libraries['/usr/lib/libocsync.so.0'].csync_get_status
csync_get_status.restype = c_int
csync_get_status.argtypes = [POINTER(CSYNC)]
csync_set_status = _libraries['/usr/lib/libocsync.so.0'].csync_set_status
csync_set_status.restype = c_int
csync_set_status.argtypes = [POINTER(CSYNC), c_int]
class csync_tree_walk_file_s(Structure):
    pass
TREE_WALK_FILE = csync_tree_walk_file_s
csync_treewalk_visit_func = CFUNCTYPE(c_int, POINTER(TREE_WALK_FILE), c_void_p)
csync_walk_local_tree = _libraries['/usr/lib/libocsync.so.0'].csync_walk_local_tree
csync_walk_local_tree.restype = c_int
csync_walk_local_tree.argtypes = [POINTER(CSYNC), POINTER(csync_treewalk_visit_func), c_int]
csync_walk_remote_tree = _libraries['/usr/lib/libocsync.so.0'].csync_walk_remote_tree
csync_walk_remote_tree.restype = c_int
csync_walk_remote_tree.argtypes = [POINTER(CSYNC), POINTER(csync_treewalk_visit_func), c_int]
csync_set_iconv_codec = _libraries['/usr/lib/libocsync.so.0'].csync_set_iconv_codec
csync_set_iconv_codec.restype = c_int
csync_set_iconv_codec.argtypes = [STRING]

# values for enumeration 'csync_error_codes_e'
CSYNC_ERR_NONE = 0
CSYNC_ERR_LOG = 1
CSYNC_ERR_LOCK = 2
CSYNC_ERR_STATEDB_LOAD = 3
CSYNC_ERR_STATEDB_WRITE = 4
CSYNC_ERR_MODULE = 5
CSYNC_ERR_TIMESKEW = 6
CSYNC_ERR_FILESYSTEM = 7
CSYNC_ERR_TREE = 8
CSYNC_ERR_MEM = 9
CSYNC_ERR_PARAM = 10
CSYNC_ERR_UPDATE = 11
CSYNC_ERR_RECONCILE = 12
CSYNC_ERR_PROPAGATE = 13
CSYNC_ERR_ACCESS_FAILED = 14
CSYNC_ERR_REMOTE_CREATE = 15
CSYNC_ERR_REMOTE_STAT = 16
CSYNC_ERR_LOCAL_CREATE = 17
CSYNC_ERR_LOCAL_STAT = 18
CSYNC_ERR_PROXY = 19
CSYNC_ERR_LOOKUP = 20
CSYNC_ERR_AUTH_SERVER = 21
CSYNC_ERR_AUTH_PROXY = 22
CSYNC_ERR_CONNECT = 23
CSYNC_ERR_TIMEOUT = 24
CSYNC_ERR_HTTP = 25
CSYNC_ERR_PERM = 26
CSYNC_ERR_NOT_FOUND = 27
CSYNC_ERR_EXISTS = 28
CSYNC_ERR_NOSPC = 29
CSYNC_ERR_QUOTA = 30
CSYNC_ERR_SERVICE_UNAVAILABLE = 31
CSYNC_ERR_FILE_TOO_BIG = 32
CSYNC_ERR_ABORTED = 33
CSYNC_ERR_UNSPEC = 34
csync_error_codes_e = c_int # enum
CSYNC_ERROR_CODE = csync_error_codes_e
csync_get_error = _libraries['/usr/lib/libocsync.so.0'].csync_get_error
csync_get_error.restype = CSYNC_ERROR_CODE
csync_get_error.argtypes = [POINTER(CSYNC)]
csync_get_error_string = _libraries['/usr/lib/libocsync.so.0'].csync_get_error_string
csync_get_error_string.restype = STRING
csync_get_error_string.argtypes = [POINTER(CSYNC)]
csync_set_module_property = _libraries['/usr/lib/libocsync.so.0'].csync_set_module_property
csync_set_module_property.restype = c_int
csync_set_module_property.argtypes = [POINTER(CSYNC), STRING, c_void_p]

# values for enumeration 'csync_notify_type_e'
CSYNC_NOTIFY_START_DOWNLOAD = 0
CSYNC_NOTIFY_START_UPLOAD = 1
CSYNC_NOTIFY_PROGRESS = 2
CSYNC_NOTIFY_FINISHED_DOWNLOAD = 3
CSYNC_NOTIFY_FINISHED_UPLOAD = 4
CSYNC_NOTIFY_ERROR = 5
csync_notify_type_e = c_int # enum
csync_progress_callback = CFUNCTYPE(None, STRING, csync_notify_type_e, c_longlong, c_longlong, c_void_p)
csync_set_progress_callback = _libraries['/usr/lib/libocsync.so.0'].csync_set_progress_callback
csync_set_progress_callback.restype = c_int
csync_set_progress_callback.argtypes = [POINTER(CSYNC), csync_progress_callback]
__ssize_t = c_long
ssize_t = __ssize_t
__read_chk = _libraries['/usr/lib/libocsync.so.0'].__read_chk
__read_chk.restype = ssize_t
__read_chk.argtypes = [c_int, c_void_p, size_t, size_t]
read = _libraries['/usr/lib/libocsync.so.0'].read
read.restype = ssize_t
read.argtypes = [c_int, c_void_p, size_t]
__off_t = c_long
__pread_chk = _libraries['/usr/lib/libocsync.so.0'].__pread_chk
__pread_chk.restype = ssize_t
__pread_chk.argtypes = [c_int, c_void_p, size_t, __off_t, size_t]
__off64_t = c_long
__pread64_chk = _libraries['/usr/lib/libocsync.so.0'].__pread64_chk
__pread64_chk.restype = ssize_t
__pread64_chk.argtypes = [c_int, c_void_p, size_t, __off64_t, size_t]
pread = _libraries['/usr/lib/libocsync.so.0'].pread
pread.restype = ssize_t
pread.argtypes = [c_int, c_void_p, size_t, __off_t]
pread64 = _libraries['/usr/lib/libocsync.so.0'].pread64
pread64.restype = ssize_t
pread64.argtypes = [c_int, c_void_p, size_t, __off64_t]
__readlink_chk = _libraries['/usr/lib/libocsync.so.0'].__readlink_chk
__readlink_chk.restype = ssize_t
__readlink_chk.argtypes = [STRING, STRING, size_t, size_t]
readlink = _libraries['/usr/lib/libocsync.so.0'].readlink
readlink.restype = ssize_t
readlink.argtypes = [STRING, STRING, size_t]
__readlinkat_chk = _libraries['/usr/lib/libocsync.so.0'].__readlinkat_chk
__readlinkat_chk.restype = ssize_t
__readlinkat_chk.argtypes = [c_int, STRING, STRING, size_t, size_t]
readlinkat = _libraries['/usr/lib/libocsync.so.0'].readlinkat
readlinkat.restype = ssize_t
readlinkat.argtypes = [c_int, STRING, STRING, size_t]
__getcwd_chk = _libraries['/usr/lib/libocsync.so.0'].__getcwd_chk
__getcwd_chk.restype = STRING
__getcwd_chk.argtypes = [STRING, size_t, size_t]
getcwd = _libraries['/usr/lib/libocsync.so.0'].getcwd
getcwd.restype = STRING
getcwd.argtypes = [STRING, size_t]
__getwd_chk = _libraries['/usr/lib/libocsync.so.0'].__getwd_chk
__getwd_chk.restype = STRING
__getwd_chk.argtypes = [STRING, size_t]
getwd = _libraries['/usr/lib/libocsync.so.0'].getwd
getwd.restype = STRING
getwd.argtypes = [STRING]
__confstr_chk = _libraries['/usr/lib/libocsync.so.0'].__confstr_chk
__confstr_chk.restype = size_t
__confstr_chk.argtypes = [c_int, STRING, size_t, size_t]
confstr = _libraries['/usr/lib/libocsync.so.0'].confstr
confstr.restype = size_t
confstr.argtypes = [c_int, STRING, size_t]
__gid_t = c_uint
__getgroups_chk = _libraries['/usr/lib/libocsync.so.0'].__getgroups_chk
__getgroups_chk.restype = c_int
__getgroups_chk.argtypes = [c_int, POINTER(__gid_t), size_t]
getgroups = _libraries['/usr/lib/libocsync.so.0'].getgroups
getgroups.restype = c_int
getgroups.argtypes = [c_int, POINTER(__gid_t)]
__ttyname_r_chk = _libraries['/usr/lib/libocsync.so.0'].__ttyname_r_chk
__ttyname_r_chk.restype = c_int
__ttyname_r_chk.argtypes = [c_int, STRING, size_t, size_t]
ttyname_r = _libraries['/usr/lib/libocsync.so.0'].ttyname_r
ttyname_r.restype = c_int
ttyname_r.argtypes = [c_int, STRING, size_t]
__getlogin_r_chk = _libraries['/usr/lib/libocsync.so.0'].__getlogin_r_chk
__getlogin_r_chk.restype = c_int
__getlogin_r_chk.argtypes = [STRING, size_t, size_t]
getlogin_r = _libraries['/usr/lib/libocsync.so.0'].getlogin_r
getlogin_r.restype = c_int
getlogin_r.argtypes = [STRING, size_t]
__gethostname_chk = _libraries['/usr/lib/libocsync.so.0'].__gethostname_chk
__gethostname_chk.restype = c_int
__gethostname_chk.argtypes = [STRING, size_t, size_t]
gethostname = _libraries['/usr/lib/libocsync.so.0'].gethostname
gethostname.restype = c_int
gethostname.argtypes = [STRING, size_t]
__getdomainname_chk = _libraries['/usr/lib/libocsync.so.0'].__getdomainname_chk
__getdomainname_chk.restype = c_int
__getdomainname_chk.argtypes = [STRING, size_t, size_t]
getdomainname = _libraries['/usr/lib/libocsync.so.0'].getdomainname
getdomainname.restype = c_int
getdomainname.argtypes = [STRING, size_t]
getopt = _libraries['/usr/lib/libocsync.so.0'].getopt
getopt.restype = c_int
getopt.argtypes = [c_int, POINTER(STRING), STRING]
class fd_set(Structure):
    pass
class timeval(Structure):
    pass
select = _libraries['/usr/lib/libocsync.so.0'].select
select.restype = c_int
select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
class timespec(Structure):
    pass
__time_t = c_long
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', c_long),
]
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
pselect = _libraries['/usr/lib/libocsync.so.0'].pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
gnu_dev_major = _libraries['/usr/lib/libocsync.so.0'].gnu_dev_major
gnu_dev_major.restype = c_uint
gnu_dev_major.argtypes = [c_ulonglong]
gnu_dev_minor = _libraries['/usr/lib/libocsync.so.0'].gnu_dev_minor
gnu_dev_minor.restype = c_uint
gnu_dev_minor.argtypes = [c_ulonglong]
gnu_dev_makedev = _libraries['/usr/lib/libocsync.so.0'].gnu_dev_makedev
gnu_dev_makedev.restype = c_ulonglong
gnu_dev_makedev.argtypes = [c_uint, c_uint]
access = _libraries['/usr/lib/libocsync.so.0'].access
access.restype = c_int
access.argtypes = [STRING, c_int]
euidaccess = _libraries['/usr/lib/libocsync.so.0'].euidaccess
euidaccess.restype = c_int
euidaccess.argtypes = [STRING, c_int]
eaccess = _libraries['/usr/lib/libocsync.so.0'].eaccess
eaccess.restype = c_int
eaccess.argtypes = [STRING, c_int]
faccessat = _libraries['/usr/lib/libocsync.so.0'].faccessat
faccessat.restype = c_int
faccessat.argtypes = [c_int, STRING, c_int, c_int]
lseek = _libraries['/usr/lib/libocsync.so.0'].lseek
lseek.restype = __off_t
lseek.argtypes = [c_int, __off_t, c_int]
lseek64 = _libraries['/usr/lib/libocsync.so.0'].lseek64
lseek64.restype = __off64_t
lseek64.argtypes = [c_int, __off64_t, c_int]
close = _libraries['/usr/lib/libocsync.so.0'].close
close.restype = c_int
close.argtypes = [c_int]
write = _libraries['/usr/lib/libocsync.so.0'].write
write.restype = ssize_t
write.argtypes = [c_int, c_void_p, size_t]
pwrite = _libraries['/usr/lib/libocsync.so.0'].pwrite
pwrite.restype = ssize_t
pwrite.argtypes = [c_int, c_void_p, size_t, __off_t]
pwrite64 = _libraries['/usr/lib/libocsync.so.0'].pwrite64
pwrite64.restype = ssize_t
pwrite64.argtypes = [c_int, c_void_p, size_t, __off64_t]
pipe = _libraries['/usr/lib/libocsync.so.0'].pipe
pipe.restype = c_int
pipe.argtypes = [POINTER(c_int)]
pipe2 = _libraries['/usr/lib/libocsync.so.0'].pipe2
pipe2.restype = c_int
pipe2.argtypes = [POINTER(c_int), c_int]
alarm = _libraries['/usr/lib/libocsync.so.0'].alarm
alarm.restype = c_uint
alarm.argtypes = [c_uint]
sleep = _libraries['/usr/lib/libocsync.so.0'].sleep
sleep.restype = c_uint
sleep.argtypes = [c_uint]
__useconds_t = c_uint
ualarm = _libraries['/usr/lib/libocsync.so.0'].ualarm
ualarm.restype = __useconds_t
ualarm.argtypes = [__useconds_t, __useconds_t]
usleep = _libraries['/usr/lib/libocsync.so.0'].usleep
usleep.restype = c_int
usleep.argtypes = [__useconds_t]
pause = _libraries['/usr/lib/libocsync.so.0'].pause
pause.restype = c_int
pause.argtypes = []
__uid_t = c_uint
chown = _libraries['/usr/lib/libocsync.so.0'].chown
chown.restype = c_int
chown.argtypes = [STRING, __uid_t, __gid_t]
fchown = _libraries['/usr/lib/libocsync.so.0'].fchown
fchown.restype = c_int
fchown.argtypes = [c_int, __uid_t, __gid_t]
lchown = _libraries['/usr/lib/libocsync.so.0'].lchown
lchown.restype = c_int
lchown.argtypes = [STRING, __uid_t, __gid_t]
fchownat = _libraries['/usr/lib/libocsync.so.0'].fchownat
fchownat.restype = c_int
fchownat.argtypes = [c_int, STRING, __uid_t, __gid_t, c_int]
chdir = _libraries['/usr/lib/libocsync.so.0'].chdir
chdir.restype = c_int
chdir.argtypes = [STRING]
fchdir = _libraries['/usr/lib/libocsync.so.0'].fchdir
fchdir.restype = c_int
fchdir.argtypes = [c_int]
get_current_dir_name = _libraries['/usr/lib/libocsync.so.0'].get_current_dir_name
get_current_dir_name.restype = STRING
get_current_dir_name.argtypes = []
dup = _libraries['/usr/lib/libocsync.so.0'].dup
dup.restype = c_int
dup.argtypes = [c_int]
dup2 = _libraries['/usr/lib/libocsync.so.0'].dup2
dup2.restype = c_int
dup2.argtypes = [c_int, c_int]
dup3 = _libraries['/usr/lib/libocsync.so.0'].dup3
dup3.restype = c_int
dup3.argtypes = [c_int, c_int, c_int]
execve = _libraries['/usr/lib/libocsync.so.0'].execve
execve.restype = c_int
execve.argtypes = [STRING, POINTER(STRING), POINTER(STRING)]
fexecve = _libraries['/usr/lib/libocsync.so.0'].fexecve
fexecve.restype = c_int
fexecve.argtypes = [c_int, POINTER(STRING), POINTER(STRING)]
execv = _libraries['/usr/lib/libocsync.so.0'].execv
execv.restype = c_int
execv.argtypes = [STRING, POINTER(STRING)]
execle = _libraries['/usr/lib/libocsync.so.0'].execle
execle.restype = c_int
execle.argtypes = [STRING, STRING]
execl = _libraries['/usr/lib/libocsync.so.0'].execl
execl.restype = c_int
execl.argtypes = [STRING, STRING]
execvp = _libraries['/usr/lib/libocsync.so.0'].execvp
execvp.restype = c_int
execvp.argtypes = [STRING, POINTER(STRING)]
execlp = _libraries['/usr/lib/libocsync.so.0'].execlp
execlp.restype = c_int
execlp.argtypes = [STRING, STRING]
execvpe = _libraries['/usr/lib/libocsync.so.0'].execvpe
execvpe.restype = c_int
execvpe.argtypes = [STRING, POINTER(STRING), POINTER(STRING)]
nice = _libraries['/usr/lib/libocsync.so.0'].nice
nice.restype = c_int
nice.argtypes = [c_int]
_exit = _libraries['/usr/lib/libocsync.so.0']._exit
_exit.restype = None
_exit.argtypes = [c_int]
pathconf = _libraries['/usr/lib/libocsync.so.0'].pathconf
pathconf.restype = c_long
pathconf.argtypes = [STRING, c_int]
fpathconf = _libraries['/usr/lib/libocsync.so.0'].fpathconf
fpathconf.restype = c_long
fpathconf.argtypes = [c_int, c_int]
sysconf = _libraries['/usr/lib/libocsync.so.0'].sysconf
sysconf.restype = c_long
sysconf.argtypes = [c_int]
__pid_t = c_int
getpid = _libraries['/usr/lib/libocsync.so.0'].getpid
getpid.restype = __pid_t
getpid.argtypes = []
getppid = _libraries['/usr/lib/libocsync.so.0'].getppid
getppid.restype = __pid_t
getppid.argtypes = []
getpgrp = _libraries['/usr/lib/libocsync.so.0'].getpgrp
getpgrp.restype = __pid_t
getpgrp.argtypes = []
__getpgid = _libraries['/usr/lib/libocsync.so.0'].__getpgid
__getpgid.restype = __pid_t
__getpgid.argtypes = [__pid_t]
getpgid = _libraries['/usr/lib/libocsync.so.0'].getpgid
getpgid.restype = __pid_t
getpgid.argtypes = [__pid_t]
setpgid = _libraries['/usr/lib/libocsync.so.0'].setpgid
setpgid.restype = c_int
setpgid.argtypes = [__pid_t, __pid_t]
setpgrp = _libraries['/usr/lib/libocsync.so.0'].setpgrp
setpgrp.restype = c_int
setpgrp.argtypes = []
setsid = _libraries['/usr/lib/libocsync.so.0'].setsid
setsid.restype = __pid_t
setsid.argtypes = []
getsid = _libraries['/usr/lib/libocsync.so.0'].getsid
getsid.restype = __pid_t
getsid.argtypes = [__pid_t]
getuid = _libraries['/usr/lib/libocsync.so.0'].getuid
getuid.restype = __uid_t
getuid.argtypes = []
geteuid = _libraries['/usr/lib/libocsync.so.0'].geteuid
geteuid.restype = __uid_t
geteuid.argtypes = []
getgid = _libraries['/usr/lib/libocsync.so.0'].getgid
getgid.restype = __gid_t
getgid.argtypes = []
getegid = _libraries['/usr/lib/libocsync.so.0'].getegid
getegid.restype = __gid_t
getegid.argtypes = []
group_member = _libraries['/usr/lib/libocsync.so.0'].group_member
group_member.restype = c_int
group_member.argtypes = [__gid_t]
setuid = _libraries['/usr/lib/libocsync.so.0'].setuid
setuid.restype = c_int
setuid.argtypes = [__uid_t]
setreuid = _libraries['/usr/lib/libocsync.so.0'].setreuid
setreuid.restype = c_int
setreuid.argtypes = [__uid_t, __uid_t]
seteuid = _libraries['/usr/lib/libocsync.so.0'].seteuid
seteuid.restype = c_int
seteuid.argtypes = [__uid_t]
setgid = _libraries['/usr/lib/libocsync.so.0'].setgid
setgid.restype = c_int
setgid.argtypes = [__gid_t]
setregid = _libraries['/usr/lib/libocsync.so.0'].setregid
setregid.restype = c_int
setregid.argtypes = [__gid_t, __gid_t]
setegid = _libraries['/usr/lib/libocsync.so.0'].setegid
setegid.restype = c_int
setegid.argtypes = [__gid_t]
getresuid = _libraries['/usr/lib/libocsync.so.0'].getresuid
getresuid.restype = c_int
getresuid.argtypes = [POINTER(__uid_t), POINTER(__uid_t), POINTER(__uid_t)]
getresgid = _libraries['/usr/lib/libocsync.so.0'].getresgid
getresgid.restype = c_int
getresgid.argtypes = [POINTER(__gid_t), POINTER(__gid_t), POINTER(__gid_t)]
setresuid = _libraries['/usr/lib/libocsync.so.0'].setresuid
setresuid.restype = c_int
setresuid.argtypes = [__uid_t, __uid_t, __uid_t]
setresgid = _libraries['/usr/lib/libocsync.so.0'].setresgid
setresgid.restype = c_int
setresgid.argtypes = [__gid_t, __gid_t, __gid_t]
fork = _libraries['/usr/lib/libocsync.so.0'].fork
fork.restype = __pid_t
fork.argtypes = []
vfork = _libraries['/usr/lib/libocsync.so.0'].vfork
vfork.restype = __pid_t
vfork.argtypes = []
ttyname = _libraries['/usr/lib/libocsync.so.0'].ttyname
ttyname.restype = STRING
ttyname.argtypes = [c_int]
isatty = _libraries['/usr/lib/libocsync.so.0'].isatty
isatty.restype = c_int
isatty.argtypes = [c_int]
ttyslot = _libraries['/usr/lib/libocsync.so.0'].ttyslot
ttyslot.restype = c_int
ttyslot.argtypes = []
link = _libraries['/usr/lib/libocsync.so.0'].link
link.restype = c_int
link.argtypes = [STRING, STRING]
linkat = _libraries['/usr/lib/libocsync.so.0'].linkat
linkat.restype = c_int
linkat.argtypes = [c_int, STRING, c_int, STRING, c_int]
symlink = _libraries['/usr/lib/libocsync.so.0'].symlink
symlink.restype = c_int
symlink.argtypes = [STRING, STRING]
symlinkat = _libraries['/usr/lib/libocsync.so.0'].symlinkat
symlinkat.restype = c_int
symlinkat.argtypes = [STRING, c_int, STRING]
unlink = _libraries['/usr/lib/libocsync.so.0'].unlink
unlink.restype = c_int
unlink.argtypes = [STRING]
unlinkat = _libraries['/usr/lib/libocsync.so.0'].unlinkat
unlinkat.restype = c_int
unlinkat.argtypes = [c_int, STRING, c_int]
rmdir = _libraries['/usr/lib/libocsync.so.0'].rmdir
rmdir.restype = c_int
rmdir.argtypes = [STRING]
tcgetpgrp = _libraries['/usr/lib/libocsync.so.0'].tcgetpgrp
tcgetpgrp.restype = __pid_t
tcgetpgrp.argtypes = [c_int]
tcsetpgrp = _libraries['/usr/lib/libocsync.so.0'].tcsetpgrp
tcsetpgrp.restype = c_int
tcsetpgrp.argtypes = [c_int, __pid_t]
getlogin = _libraries['/usr/lib/libocsync.so.0'].getlogin
getlogin.restype = STRING
getlogin.argtypes = []
setlogin = _libraries['/usr/lib/libocsync.so.0'].setlogin
setlogin.restype = c_int
setlogin.argtypes = [STRING]
sethostname = _libraries['/usr/lib/libocsync.so.0'].sethostname
sethostname.restype = c_int
sethostname.argtypes = [STRING, size_t]
sethostid = _libraries['/usr/lib/libocsync.so.0'].sethostid
sethostid.restype = c_int
sethostid.argtypes = [c_long]
setdomainname = _libraries['/usr/lib/libocsync.so.0'].setdomainname
setdomainname.restype = c_int
setdomainname.argtypes = [STRING, size_t]
vhangup = _libraries['/usr/lib/libocsync.so.0'].vhangup
vhangup.restype = c_int
vhangup.argtypes = []
revoke = _libraries['/usr/lib/libocsync.so.0'].revoke
revoke.restype = c_int
revoke.argtypes = [STRING]
profil = _libraries['/usr/lib/libocsync.so.0'].profil
profil.restype = c_int
profil.argtypes = [POINTER(c_ushort), size_t, size_t, c_uint]
acct = _libraries['/usr/lib/libocsync.so.0'].acct
acct.restype = c_int
acct.argtypes = [STRING]
getusershell = _libraries['/usr/lib/libocsync.so.0'].getusershell
getusershell.restype = STRING
getusershell.argtypes = []
endusershell = _libraries['/usr/lib/libocsync.so.0'].endusershell
endusershell.restype = None
endusershell.argtypes = []
setusershell = _libraries['/usr/lib/libocsync.so.0'].setusershell
setusershell.restype = None
setusershell.argtypes = []
daemon = _libraries['/usr/lib/libocsync.so.0'].daemon
daemon.restype = c_int
daemon.argtypes = [c_int, c_int]
chroot = _libraries['/usr/lib/libocsync.so.0'].chroot
chroot.restype = c_int
chroot.argtypes = [STRING]
getpass = _libraries['/usr/lib/libocsync.so.0'].getpass
getpass.restype = STRING
getpass.argtypes = [STRING]
fsync = _libraries['/usr/lib/libocsync.so.0'].fsync
fsync.restype = c_int
fsync.argtypes = [c_int]
gethostid = _libraries['/usr/lib/libocsync.so.0'].gethostid
gethostid.restype = c_long
gethostid.argtypes = []
sync = _libraries['/usr/lib/libocsync.so.0'].sync
sync.restype = None
sync.argtypes = []
getpagesize = _libraries['/usr/lib/libocsync.so.0'].getpagesize
getpagesize.restype = c_int
getpagesize.argtypes = []
getdtablesize = _libraries['/usr/lib/libocsync.so.0'].getdtablesize
getdtablesize.restype = c_int
getdtablesize.argtypes = []
truncate = _libraries['/usr/lib/libocsync.so.0'].truncate
truncate.restype = c_int
truncate.argtypes = [STRING, __off_t]
truncate64 = _libraries['/usr/lib/libocsync.so.0'].truncate64
truncate64.restype = c_int
truncate64.argtypes = [STRING, __off64_t]
ftruncate = _libraries['/usr/lib/libocsync.so.0'].ftruncate
ftruncate.restype = c_int
ftruncate.argtypes = [c_int, __off_t]
ftruncate64 = _libraries['/usr/lib/libocsync.so.0'].ftruncate64
ftruncate64.restype = c_int
ftruncate64.argtypes = [c_int, __off64_t]
brk = _libraries['/usr/lib/libocsync.so.0'].brk
brk.restype = c_int
brk.argtypes = [c_void_p]
intptr_t = c_long
sbrk = _libraries['/usr/lib/libocsync.so.0'].sbrk
sbrk.restype = c_void_p
sbrk.argtypes = [intptr_t]
syscall = _libraries['/usr/lib/libocsync.so.0'].syscall
syscall.restype = c_long
syscall.argtypes = [c_long]
lockf = _libraries['/usr/lib/libocsync.so.0'].lockf
lockf.restype = c_int
lockf.argtypes = [c_int, c_int, __off_t]
lockf64 = _libraries['/usr/lib/libocsync.so.0'].lockf64
lockf64.restype = c_int
lockf64.argtypes = [c_int, c_int, __off64_t]
fdatasync = _libraries['/usr/lib/libocsync.so.0'].fdatasync
fdatasync.restype = c_int
fdatasync.argtypes = [c_int]
swab = _libraries['/usr/lib/libocsync.so.0'].swab
swab.restype = None
swab.argtypes = [c_void_p, c_void_p, ssize_t]
ctermid = _libraries['/usr/lib/libocsync.so.0'].ctermid
ctermid.restype = STRING
ctermid.argtypes = [STRING]
time_t = __time_t
uid_t = __uid_t
gid_t = __gid_t
__mode_t = c_uint
mode_t = __mode_t

# values for enumeration 'csync_ftw_type_e'
CSYNC_FTW_TYPE_FILE = 0
CSYNC_FTW_TYPE_SLINK = 1
CSYNC_FTW_TYPE_DIR = 2
csync_ftw_type_e = c_int # enum

# values for enumeration 'csync_instructions_e'
CSYNC_INSTRUCTION_NONE = 0
CSYNC_INSTRUCTION_EVAL = 1
CSYNC_INSTRUCTION_REMOVE = 2
CSYNC_INSTRUCTION_RENAME = 4
CSYNC_INSTRUCTION_NEW = 8
CSYNC_INSTRUCTION_CONFLICT = 16
CSYNC_INSTRUCTION_IGNORE = 32
CSYNC_INSTRUCTION_SYNC = 64
CSYNC_INSTRUCTION_STAT_ERROR = 128
CSYNC_INSTRUCTION_ERROR = 256
CSYNC_INSTRUCTION_DELETED = 512
CSYNC_INSTRUCTION_UPDATED = 1024
csync_instructions_e = c_int # enum
csync_tree_walk_file_s._fields_ = [
    ('path', STRING),
    ('modtime', time_t),
    ('uid', uid_t),
    ('gid', gid_t),
    ('mode', mode_t),
    ('type', csync_ftw_type_e),
    ('instruction', csync_instructions_e),
    ('rename_path', STRING),
]
csync_s._fields_ = [
]
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
__fd_mask = c_long
fd_set._fields_ = [
    ('fds_bits', __fd_mask * 16),
]
__all__ = ['lseek64', 'lseek', 'CSYNC_ERR_LOCAL_CREATE',
           'csync_set_log_callback', 'seteuid',
           'CSYNC_ERR_ACCESS_FAILED', 'isatty', 'CSYNC_ERR_TIMESKEW',
           'execle', 'csync_is_statedb_disabled', 'truncate64',
           '__time_t', 'CSYNC_FTW_TYPE_SLINK', 'sleep', 'lockf64',
           'mode_t', '__off64_t', 'size_t', 'csync_walk_local_tree',
           'getegid', 'csync_error_codes_e', 'group_member',
           'CSYNC_ERR_STATEDB_LOAD', 'get_current_dir_name',
           'csync_update', 'pause', 'csync_set_auth_callback',
           'csync_add_exclude_list', 'getresgid', 'sethostname',
           'CSYNC_NOTIFY_PROGRESS', 'CSYNC_ERR_CONNECT',
           'CSYNC_ERR_UNSPEC', 'CSYNC_ERR_HTTP', 'fpathconf',
           '__getpgid', 'csync_set_status', 'lchown', 'setgid',
           'csync_get_error', 'CSYNC_ERR_NONE', 'getusershell',
           'CSYNC_ERR_LOCAL_STAT', 'CSYNC_INSTRUCTION_NONE',
           'CSYNC_NOTIFY_FINISHED_UPLOAD', 'getlogin',
           'csync_progress_callback', 'intptr_t',
           'csync_walk_remote_tree', 'dup3', 'dup2', 'read',
           'getppid', 'CSYNC_INSTRUCTION_REMOVE', 'getdomainname',
           'fchown', 'getpgrp', 'CSYNC_NOTIFY_FINISHED_DOWNLOAD',
           'CSYNC_NOTIFY_START_DOWNLOAD', 'csync_get_error_string',
           'gnu_dev_minor', 'execl', 'readlinkat', 'daemon', 'fsync',
           'csync_set_module_property', 'CSYNC_INSTRUCTION_DELETED',
           'tcsetpgrp', 'setreuid', 'csync_destroy',
           'CSYNC_ERR_PROXY', 'CSYNC_NOTIFY_ERROR', 'getpagesize',
           'setlogin', 'execv', 'nice', 'gnu_dev_makedev', 'ttyname',
           'linkat', 'getlogin_r', 'CSYNC_ERR_RECONCILE', '__ssize_t',
           '__confstr_chk', 'CSYNC_ERR_SERVICE_UNAVAILABLE',
           'csync_set_config_dir', 'CSYNC_ERR_TIMEOUT', 'sync',
           '__fd_mask', 'CSYNC_INSTRUCTION_STAT_ERROR', 'getresuid',
           'fchownat', '__pid_t', 'execlp', 'csync_get_userdata',
           'getgid', 'CSYNC_ERR_TREE', 'CSYNC_ERR_REMOTE_STAT',
           'CSYNC_INSTRUCTION_EVAL', '__sigset_t',
           'csync_get_log_callback', '__useconds_t',
           'CSYNC_ERR_REMOTE_CREATE', 'CSYNC', 'csync_get_config_dir',
           'CSYNC_ERR_AUTH_SERVER', 'csync_log_callback', 'access',
           'setsid', '__ttyname_r_chk', 'select', 'acct',
           'CSYNC_ERR_FILESYSTEM', 'ualarm', 'CSYNC_ERR_MEM',
           'revoke', 'csync_s', '__pread64_chk', 'usleep', 'setpgid',
           'setresgid', 'getcwd', 'symlink', 'pwrite64',
           '__getgroups_chk', 'CSYNC_INSTRUCTION_ERROR', 'setregid',
           'fchdir', 'ftruncate', 'setegid', 'csync_version',
           'CSYNC_FTW_TYPE_DIR', 'CSYNC_INSTRUCTION_IGNORE',
           'vhangup', 'getsid', 'csync_notify_type_e',
           'CSYNC_INSTRUCTION_RENAME', 'symlinkat',
           'CSYNC_ERR_FILE_TOO_BIG', 'pipe2', 'sethostid',
           'CSYNC_INSTRUCTION_UPDATED', 'fd_set',
           'csync_set_log_verbosity', '_exit', '__readlink_chk',
           'endusershell', 'confstr', 'csync_treewalk_visit_func',
           '__read_chk', '__mode_t', 'swab', 'csync_get_status',
           'getpgid', 'brk', '__off_t', 'gethostid', 'pread',
           '__readlinkat_chk', 'getdtablesize', 'ttyname_r',
           '__gid_t', 'gethostname', 'timespec', 'CSYNC_ERR_EXISTS',
           'faccessat', 'gnu_dev_major', 'rmdir', 'dup',
           'csync_propagate', 'fdatasync', 'CSYNC_ERR_PARAM',
           'csync_reconcile', '__pread_chk', 'execvpe',
           'csync_ftw_type_e', 'eaccess', 'execvp', 'ftruncate64',
           '__getlogin_r_chk', 'link', 'uid_t',
           'csync_set_progress_callback', '__getcwd_chk', 'pselect',
           'gid_t', 'CSYNC_ERR_PROPAGATE', 'execve', 'getpass',
           'CSYNC_ERR_AUTH_PROXY', 'chdir', '__suseconds_t', 'sbrk',
           '__getwd_chk', 'CSYNC_INSTRUCTION_SYNC',
           'csync_get_statedb_file', 'CSYNC_ERR_NOSPC', 'setresuid',
           'csync_auth_callback', 'fexecve', 'vfork', 'setuid',
           'fork', 'csync_enable_conflictcopys', 'lockf', 'sysconf',
           'syscall', 'csync_set_iconv_codec', 'getwd',
           'setdomainname', 'pread64', 'euidaccess', 'close',
           'csync_enable_statedb', 'CSYNC_ERR_LOG',
           'csync_instructions_e', 'time_t', '__gethostname_chk',
           'chroot', 'csync_tree_walk_file_s', 'getgroups',
           'TREE_WALK_FILE', 'ssize_t', 'csync_disable_statedb',
           'setpgrp', 'timeval', 'write', 'csync_get_auth_callback',
           'CSYNC_NOTIFY_START_UPLOAD', 'getopt', 'CSYNC_ERR_LOCK',
           'csync_get_log_verbosity', 'CSYNC_FTW_TYPE_FILE',
           'CSYNC_ERR_LOOKUP', 'CSYNC_ERR_PERM',
           'CSYNC_INSTRUCTION_CONFLICT', 'pathconf',
           'csync_set_userdata', 'truncate', 'CSYNC_ERR_NOT_FOUND',
           'CSYNC_ERROR_CODE', 'CSYNC_ERR_QUOTA', 'getpid',
           'setusershell', 'readlink', 'CSYNC_ERR_MODULE', 'unlink',
           'tcgetpgrp', 'unlinkat', '__getdomainname_chk', 'ttyslot',
           'pwrite', 'getuid', 'csync_create', 'alarm',
           'csync_get_local_only', 'csync_init', 'pipe', 'ctermid',
           'chown', 'CSYNC_ERR_UPDATE', 'CSYNC_INSTRUCTION_NEW',
           'csync_set_local_only', '__uid_t', 'profil', 'geteuid']
