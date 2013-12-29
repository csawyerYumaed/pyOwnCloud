from ctypes import *
from .pre import _lib

STRING = c_char_p

class csync_s(Structure):
	pass

csync_ftw_type_e = c_int # enum
csync_instructions_e = c_int # enum
csync_notify_type_e = c_int # enum
csync_error_codes_e = c_int # enum

CSYNC = csync_s
csync_create = _lib.csync_create
csync_create.restype = c_int
csync_create.argtypes = [POINTER(POINTER(CSYNC)), STRING, STRING]
csync_init = _lib.csync_init
csync_init.restype = c_int
csync_init.argtypes = [POINTER(CSYNC)]
csync_update = _lib.csync_update
csync_update.restype = c_int
csync_update.argtypes = [POINTER(CSYNC)]
csync_reconcile = _lib.csync_reconcile
csync_reconcile.restype = c_int
csync_reconcile.argtypes = [POINTER(CSYNC)]
#csync_propagate = _lib.csync_propagate
#csync_propagate.restype = c_int
#csync_propagate.argtypes = [POINTER(CSYNC)]
csync_destroy = _lib.csync_destroy
csync_destroy.restype = c_int
csync_destroy.argtypes = [POINTER(CSYNC)]
csync_add_exclude_list = _lib.csync_add_exclude_list
csync_add_exclude_list.restype = c_int
csync_add_exclude_list.argtypes = [POINTER(CSYNC), STRING]
csync_get_config_dir = _lib.csync_get_config_dir
csync_get_config_dir.restype = STRING
csync_get_config_dir.argtypes = [POINTER(CSYNC)]
csync_set_config_dir = _lib.csync_set_config_dir
csync_set_config_dir.restype = c_int
csync_set_config_dir.argtypes = [POINTER(CSYNC), STRING]
csync_enable_statedb = _lib.csync_enable_statedb
csync_enable_statedb.restype = c_int
csync_enable_statedb.argtypes = [POINTER(CSYNC)]
csync_disable_statedb = _lib.csync_disable_statedb
csync_disable_statedb.restype = c_int
csync_disable_statedb.argtypes = [POINTER(CSYNC)]
csync_is_statedb_disabled = _lib.csync_is_statedb_disabled
csync_is_statedb_disabled.restype = c_int
csync_is_statedb_disabled.argtypes = [POINTER(CSYNC)]
csync_get_userdata = _lib.csync_get_userdata
csync_get_userdata.restype = c_void_p
csync_get_userdata.argtypes = [POINTER(CSYNC)]
csync_set_userdata = _lib.csync_set_userdata
csync_set_userdata.restype = c_int
csync_set_userdata.argtypes = [POINTER(CSYNC), c_void_p]
size_t = c_ulong
csync_auth_callback = CFUNCTYPE(c_int, STRING, c_void_p, size_t, c_int, c_int, c_void_p)
csync_get_auth_callback = _lib.csync_get_auth_callback
csync_get_auth_callback.restype = csync_auth_callback
csync_get_auth_callback.argtypes = [POINTER(CSYNC)]
csync_set_auth_callback = _lib.csync_set_auth_callback
csync_set_auth_callback.restype = c_int
csync_set_auth_callback.argtypes = [POINTER(CSYNC), csync_auth_callback]
csync_get_statedb_file = _lib.csync_get_statedb_file
csync_get_statedb_file.restype = STRING
csync_get_statedb_file.argtypes = [POINTER(CSYNC)]
csync_enable_conflictcopys = _lib.csync_enable_conflictcopys
csync_enable_conflictcopys.restype = c_int
csync_enable_conflictcopys.argtypes = [POINTER(CSYNC)]
csync_set_local_only = _lib.csync_set_local_only
csync_set_local_only.restype = c_int
csync_set_local_only.argtypes = [POINTER(CSYNC), c_bool]
csync_get_local_only = _lib.csync_get_local_only
csync_get_local_only.restype = c_bool
csync_get_local_only.argtypes = [POINTER(CSYNC)]
csync_get_status = _lib.csync_get_status
csync_get_status.restype = c_int
csync_get_status.argtypes = [POINTER(CSYNC)]
csync_set_status = _lib.csync_set_status
csync_set_status.restype = c_int
csync_set_status.argtypes = [POINTER(CSYNC), c_int]
class csync_tree_walk_file_s(Structure):
	pass
TREE_WALK_FILE = csync_tree_walk_file_s
csync_treewalk_visit_func = CFUNCTYPE(c_int, POINTER(TREE_WALK_FILE), c_void_p)
csync_walk_local_tree = _lib.csync_walk_local_tree
csync_walk_local_tree.restype = c_int
csync_walk_local_tree.argtypes = [POINTER(CSYNC), POINTER(csync_treewalk_visit_func), c_int]
csync_walk_remote_tree = _lib.csync_walk_remote_tree
csync_walk_remote_tree.restype = c_int
csync_walk_remote_tree.argtypes = [POINTER(CSYNC), POINTER(csync_treewalk_visit_func), c_int]
csync_set_iconv_codec = _lib.csync_set_iconv_codec
csync_set_iconv_codec.restype = c_int
csync_set_iconv_codec.argtypes = [STRING]
class csync_progress_s(Structure):
	pass
CSYNC_PROGRESS = csync_progress_s
csync_progress_callback = CFUNCTYPE(None, POINTER(CSYNC_PROGRESS), c_void_p)
csync_set_progress_callback = _lib.csync_set_progress_callback
csync_set_progress_callback.restype = c_int
csync_set_progress_callback.argtypes = [POINTER(CSYNC), csync_progress_callback]
csync_get_progress_callback = _lib.csync_get_progress_callback
csync_get_progress_callback.restype = csync_progress_callback
csync_get_progress_callback.argtypes = [POINTER(CSYNC)]

CSYNC_ERROR_CODE = csync_error_codes_e
#csync_get_error = _lib.csync_get_error
#csync_get_error.restype = CSYNC_ERROR_CODE
#csync_get_error.argtypes = [POINTER(CSYNC)]
#csync_get_error_string = _lib.csync_get_error_string
#csync_get_error_string.restype = STRING
#csync_get_error_string.argtypes = [POINTER(CSYNC)]
csync_set_module_property = _lib.csync_set_module_property
csync_set_module_property.restype = c_int
csync_set_module_property.argtypes = [POINTER(CSYNC), STRING, c_void_p]

__ssize_t = c_long
ssize_t = __ssize_t
__read_chk = _lib.__read_chk
__read_chk.restype = ssize_t
__read_chk.argtypes = [c_int, c_void_p, size_t, size_t]
read = _lib.read
read.restype = ssize_t
read.argtypes = [c_int, c_void_p, size_t]
__off_t = c_long
__pread_chk = _lib.__pread_chk
__pread_chk.restype = ssize_t
__pread_chk.argtypes = [c_int, c_void_p, size_t, __off_t, size_t]
__off64_t = c_long
__pread64_chk = _lib.__pread64_chk
__pread64_chk.restype = ssize_t
__pread64_chk.argtypes = [c_int, c_void_p, size_t, __off64_t, size_t]
pread = _lib.pread
pread.restype = ssize_t
pread.argtypes = [c_int, c_void_p, size_t, __off_t]
pread64 = _lib.pread64
pread64.restype = ssize_t
pread64.argtypes = [c_int, c_void_p, size_t, __off64_t]
__readlink_chk = _lib.__readlink_chk
__readlink_chk.restype = ssize_t
__readlink_chk.argtypes = [STRING, STRING, size_t, size_t]
readlink = _lib.readlink
readlink.restype = ssize_t
readlink.argtypes = [STRING, STRING, size_t]
__readlinkat_chk = _lib.__readlinkat_chk
__readlinkat_chk.restype = ssize_t
__readlinkat_chk.argtypes = [c_int, STRING, STRING, size_t, size_t]
readlinkat = _lib.readlinkat
readlinkat.restype = ssize_t
readlinkat.argtypes = [c_int, STRING, STRING, size_t]
__getcwd_chk = _lib.__getcwd_chk
__getcwd_chk.restype = STRING
__getcwd_chk.argtypes = [STRING, size_t, size_t]
getcwd = _lib.getcwd
getcwd.restype = STRING
getcwd.argtypes = [STRING, size_t]
__getwd_chk = _lib.__getwd_chk
__getwd_chk.restype = STRING
__getwd_chk.argtypes = [STRING, size_t]
getwd = _lib.getwd
getwd.restype = STRING
getwd.argtypes = [STRING]
__confstr_chk = _lib.__confstr_chk
__confstr_chk.restype = size_t
__confstr_chk.argtypes = [c_int, STRING, size_t, size_t]
confstr = _lib.confstr
confstr.restype = size_t
confstr.argtypes = [c_int, STRING, size_t]
__gid_t = c_uint
__getgroups_chk = _lib.__getgroups_chk
__getgroups_chk.restype = c_int
__getgroups_chk.argtypes = [c_int, POINTER(__gid_t), size_t]
getgroups = _lib.getgroups
getgroups.restype = c_int
getgroups.argtypes = [c_int, POINTER(__gid_t)]
__ttyname_r_chk = _lib.__ttyname_r_chk
__ttyname_r_chk.restype = c_int
__ttyname_r_chk.argtypes = [c_int, STRING, size_t, size_t]
ttyname_r = _lib.ttyname_r
ttyname_r.restype = c_int
ttyname_r.argtypes = [c_int, STRING, size_t]
__getlogin_r_chk = _lib.__getlogin_r_chk
__getlogin_r_chk.restype = c_int
__getlogin_r_chk.argtypes = [STRING, size_t, size_t]
getlogin_r = _lib.getlogin_r
getlogin_r.restype = c_int
getlogin_r.argtypes = [STRING, size_t]
__gethostname_chk = _lib.__gethostname_chk
__gethostname_chk.restype = c_int
__gethostname_chk.argtypes = [STRING, size_t, size_t]
gethostname = _lib.gethostname
gethostname.restype = c_int
gethostname.argtypes = [STRING, size_t]
__getdomainname_chk = _lib.__getdomainname_chk
__getdomainname_chk.restype = c_int
__getdomainname_chk.argtypes = [STRING, size_t, size_t]
getdomainname = _lib.getdomainname
getdomainname.restype = c_int
getdomainname.argtypes = [STRING, size_t]
getopt = _lib.getopt
getopt.restype = c_int
getopt.argtypes = [c_int, POINTER(STRING), STRING]
class fd_set(Structure):
	pass
class timeval(Structure):
	pass
select = _lib.select
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
pselect = _lib.pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
gnu_dev_major = _lib.gnu_dev_major
gnu_dev_major.restype = c_uint
gnu_dev_major.argtypes = [c_ulonglong]
gnu_dev_minor = _lib.gnu_dev_minor
gnu_dev_minor.restype = c_uint
gnu_dev_minor.argtypes = [c_ulonglong]
gnu_dev_makedev = _lib.gnu_dev_makedev
gnu_dev_makedev.restype = c_ulonglong
gnu_dev_makedev.argtypes = [c_uint, c_uint]
access = _lib.access
access.restype = c_int
access.argtypes = [STRING, c_int]
euidaccess = _lib.euidaccess
euidaccess.restype = c_int
euidaccess.argtypes = [STRING, c_int]
eaccess = _lib.eaccess
eaccess.restype = c_int
eaccess.argtypes = [STRING, c_int]
faccessat = _lib.faccessat
faccessat.restype = c_int
faccessat.argtypes = [c_int, STRING, c_int, c_int]
lseek = _lib.lseek
lseek.restype = __off_t
lseek.argtypes = [c_int, __off_t, c_int]
lseek64 = _lib.lseek64
lseek64.restype = __off64_t
lseek64.argtypes = [c_int, __off64_t, c_int]
close = _lib.close
close.restype = c_int
close.argtypes = [c_int]
write = _lib.write
write.restype = ssize_t
write.argtypes = [c_int, c_void_p, size_t]
pwrite = _lib.pwrite
pwrite.restype = ssize_t
pwrite.argtypes = [c_int, c_void_p, size_t, __off_t]
pwrite64 = _lib.pwrite64
pwrite64.restype = ssize_t
pwrite64.argtypes = [c_int, c_void_p, size_t, __off64_t]
pipe = _lib.pipe
pipe.restype = c_int
pipe.argtypes = [POINTER(c_int)]
pipe2 = _lib.pipe2
pipe2.restype = c_int
pipe2.argtypes = [POINTER(c_int), c_int]
alarm = _lib.alarm
alarm.restype = c_uint
alarm.argtypes = [c_uint]
sleep = _lib.sleep
sleep.restype = c_uint
sleep.argtypes = [c_uint]
__useconds_t = c_uint
ualarm = _lib.ualarm
ualarm.restype = __useconds_t
ualarm.argtypes = [__useconds_t, __useconds_t]
usleep = _lib.usleep
usleep.restype = c_int
usleep.argtypes = [__useconds_t]
pause = _lib.pause
pause.restype = c_int
pause.argtypes = []
__uid_t = c_uint
chown = _lib.chown
chown.restype = c_int
chown.argtypes = [STRING, __uid_t, __gid_t]
fchown = _lib.fchown
fchown.restype = c_int
fchown.argtypes = [c_int, __uid_t, __gid_t]
lchown = _lib.lchown
lchown.restype = c_int
lchown.argtypes = [STRING, __uid_t, __gid_t]
fchownat = _lib.fchownat
fchownat.restype = c_int
fchownat.argtypes = [c_int, STRING, __uid_t, __gid_t, c_int]
chdir = _lib.chdir
chdir.restype = c_int
chdir.argtypes = [STRING]
fchdir = _lib.fchdir
fchdir.restype = c_int
fchdir.argtypes = [c_int]
get_current_dir_name = _lib.get_current_dir_name
get_current_dir_name.restype = STRING
get_current_dir_name.argtypes = []
dup = _lib.dup
dup.restype = c_int
dup.argtypes = [c_int]
dup2 = _lib.dup2
dup2.restype = c_int
dup2.argtypes = [c_int, c_int]
dup3 = _lib.dup3
dup3.restype = c_int
dup3.argtypes = [c_int, c_int, c_int]
execve = _lib.execve
execve.restype = c_int
execve.argtypes = [STRING, POINTER(STRING), POINTER(STRING)]
fexecve = _lib.fexecve
fexecve.restype = c_int
fexecve.argtypes = [c_int, POINTER(STRING), POINTER(STRING)]
execv = _lib.execv
execv.restype = c_int
execv.argtypes = [STRING, POINTER(STRING)]
execle = _lib.execle
execle.restype = c_int
execle.argtypes = [STRING, STRING]
execl = _lib.execl
execl.restype = c_int
execl.argtypes = [STRING, STRING]
execvp = _lib.execvp
execvp.restype = c_int
execvp.argtypes = [STRING, POINTER(STRING)]
execlp = _lib.execlp
execlp.restype = c_int
execlp.argtypes = [STRING, STRING]
execvpe = _lib.execvpe
execvpe.restype = c_int
execvpe.argtypes = [STRING, POINTER(STRING), POINTER(STRING)]
nice = _lib.nice
nice.restype = c_int
nice.argtypes = [c_int]
_exit = _lib._exit
_exit.restype = None
_exit.argtypes = [c_int]
pathconf = _lib.pathconf
pathconf.restype = c_long
pathconf.argtypes = [STRING, c_int]
fpathconf = _lib.fpathconf
fpathconf.restype = c_long
fpathconf.argtypes = [c_int, c_int]
sysconf = _lib.sysconf
sysconf.restype = c_long
sysconf.argtypes = [c_int]
__pid_t = c_int
getpid = _lib.getpid
getpid.restype = __pid_t
getpid.argtypes = []
getppid = _lib.getppid
getppid.restype = __pid_t
getppid.argtypes = []
getpgrp = _lib.getpgrp
getpgrp.restype = __pid_t
getpgrp.argtypes = []
__getpgid = _lib.__getpgid
__getpgid.restype = __pid_t
__getpgid.argtypes = [__pid_t]
getpgid = _lib.getpgid
getpgid.restype = __pid_t
getpgid.argtypes = [__pid_t]
setpgid = _lib.setpgid
setpgid.restype = c_int
setpgid.argtypes = [__pid_t, __pid_t]
setpgrp = _lib.setpgrp
setpgrp.restype = c_int
setpgrp.argtypes = []
setsid = _lib.setsid
setsid.restype = __pid_t
setsid.argtypes = []
getsid = _lib.getsid
getsid.restype = __pid_t
getsid.argtypes = [__pid_t]
getuid = _lib.getuid
getuid.restype = __uid_t
getuid.argtypes = []
geteuid = _lib.geteuid
geteuid.restype = __uid_t
geteuid.argtypes = []
getgid = _lib.getgid
getgid.restype = __gid_t
getgid.argtypes = []
getegid = _lib.getegid
getegid.restype = __gid_t
getegid.argtypes = []
group_member = _lib.group_member
group_member.restype = c_int
group_member.argtypes = [__gid_t]
setuid = _lib.setuid
setuid.restype = c_int
setuid.argtypes = [__uid_t]
setreuid = _lib.setreuid
setreuid.restype = c_int
setreuid.argtypes = [__uid_t, __uid_t]
seteuid = _lib.seteuid
seteuid.restype = c_int
seteuid.argtypes = [__uid_t]
setgid = _lib.setgid
setgid.restype = c_int
setgid.argtypes = [__gid_t]
setregid = _lib.setregid
setregid.restype = c_int
setregid.argtypes = [__gid_t, __gid_t]
setegid = _lib.setegid
setegid.restype = c_int
setegid.argtypes = [__gid_t]
getresuid = _lib.getresuid
getresuid.restype = c_int
getresuid.argtypes = [POINTER(__uid_t), POINTER(__uid_t), POINTER(__uid_t)]
getresgid = _lib.getresgid
getresgid.restype = c_int
getresgid.argtypes = [POINTER(__gid_t), POINTER(__gid_t), POINTER(__gid_t)]
setresuid = _lib.setresuid
setresuid.restype = c_int
setresuid.argtypes = [__uid_t, __uid_t, __uid_t]
setresgid = _lib.setresgid
setresgid.restype = c_int
setresgid.argtypes = [__gid_t, __gid_t, __gid_t]
fork = _lib.fork
fork.restype = __pid_t
fork.argtypes = []
vfork = _lib.vfork
vfork.restype = __pid_t
vfork.argtypes = []
ttyname = _lib.ttyname
ttyname.restype = STRING
ttyname.argtypes = [c_int]
isatty = _lib.isatty
isatty.restype = c_int
isatty.argtypes = [c_int]
ttyslot = _lib.ttyslot
ttyslot.restype = c_int
ttyslot.argtypes = []
link = _lib.link
link.restype = c_int
link.argtypes = [STRING, STRING]
linkat = _lib.linkat
linkat.restype = c_int
linkat.argtypes = [c_int, STRING, c_int, STRING, c_int]
symlink = _lib.symlink
symlink.restype = c_int
symlink.argtypes = [STRING, STRING]
symlinkat = _lib.symlinkat
symlinkat.restype = c_int
symlinkat.argtypes = [STRING, c_int, STRING]
unlink = _lib.unlink
unlink.restype = c_int
unlink.argtypes = [STRING]
unlinkat = _lib.unlinkat
unlinkat.restype = c_int
unlinkat.argtypes = [c_int, STRING, c_int]
rmdir = _lib.rmdir
rmdir.restype = c_int
rmdir.argtypes = [STRING]
tcgetpgrp = _lib.tcgetpgrp
tcgetpgrp.restype = __pid_t
tcgetpgrp.argtypes = [c_int]
tcsetpgrp = _lib.tcsetpgrp
tcsetpgrp.restype = c_int
tcsetpgrp.argtypes = [c_int, __pid_t]
getlogin = _lib.getlogin
getlogin.restype = STRING
getlogin.argtypes = []
setlogin = _lib.setlogin
setlogin.restype = c_int
setlogin.argtypes = [STRING]
sethostname = _lib.sethostname
sethostname.restype = c_int
sethostname.argtypes = [STRING, size_t]
sethostid = _lib.sethostid
sethostid.restype = c_int
sethostid.argtypes = [c_long]
setdomainname = _lib.setdomainname
setdomainname.restype = c_int
setdomainname.argtypes = [STRING, size_t]
vhangup = _lib.vhangup
vhangup.restype = c_int
vhangup.argtypes = []
revoke = _lib.revoke
revoke.restype = c_int
revoke.argtypes = [STRING]
profil = _lib.profil
profil.restype = c_int
profil.argtypes = [POINTER(c_ushort), size_t, size_t, c_uint]
acct = _lib.acct
acct.restype = c_int
acct.argtypes = [STRING]
getusershell = _lib.getusershell
getusershell.restype = STRING
getusershell.argtypes = []
endusershell = _lib.endusershell
endusershell.restype = None
endusershell.argtypes = []
setusershell = _lib.setusershell
setusershell.restype = None
setusershell.argtypes = []
daemon = _lib.daemon
daemon.restype = c_int
daemon.argtypes = [c_int, c_int]
chroot = _lib.chroot
chroot.restype = c_int
chroot.argtypes = [STRING]
getpass = _lib.getpass
getpass.restype = STRING
getpass.argtypes = [STRING]
fsync = _lib.fsync
fsync.restype = c_int
fsync.argtypes = [c_int]
gethostid = _lib.gethostid
gethostid.restype = c_long
gethostid.argtypes = []
sync = _lib.sync
sync.restype = None
sync.argtypes = []
getpagesize = _lib.getpagesize
getpagesize.restype = c_int
getpagesize.argtypes = []
getdtablesize = _lib.getdtablesize
getdtablesize.restype = c_int
getdtablesize.argtypes = []
truncate = _lib.truncate
truncate.restype = c_int
truncate.argtypes = [STRING, __off_t]
truncate64 = _lib.truncate64
truncate64.restype = c_int
truncate64.argtypes = [STRING, __off64_t]
ftruncate = _lib.ftruncate
ftruncate.restype = c_int
ftruncate.argtypes = [c_int, __off_t]
ftruncate64 = _lib.ftruncate64
ftruncate64.restype = c_int
ftruncate64.argtypes = [c_int, __off64_t]
brk = _lib.brk
brk.restype = c_int
brk.argtypes = [c_void_p]
intptr_t = c_long
sbrk = _lib.sbrk
sbrk.restype = c_void_p
sbrk.argtypes = [intptr_t]
syscall = _lib.syscall
syscall.restype = c_long
syscall.argtypes = [c_long]
lockf = _lib.lockf
lockf.restype = c_int
lockf.argtypes = [c_int, c_int, __off_t]
lockf64 = _lib.lockf64
lockf64.restype = c_int
lockf64.argtypes = [c_int, c_int, __off64_t]
fdatasync = _lib.fdatasync
fdatasync.restype = c_int
fdatasync.argtypes = [c_int]
swab = _lib.swab
swab.restype = None
swab.argtypes = [c_void_p, c_void_p, ssize_t]
ctermid = _lib.ctermid
ctermid.restype = STRING
ctermid.argtypes = [STRING]
time_t = __time_t
uid_t = __uid_t
gid_t = __gid_t
__mode_t = c_uint
mode_t = __mode_t

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
csync_progress_s._fields_ = [
	('kind', csync_notify_type_e),
	('path', STRING),
	("curr_bytes", c_int),
	("file_size", c_int),
	("overall_transmission_size", c_int),
	("current_overall_bytes", c_int),
	("overall_file_count", c_int),
	("current_file_no", c_int),
]
#csync_s._fields_ = [
#]
__suseconds_t = c_long
timeval._fields_ = [
	('tv_sec', __time_t),
	('tv_usec', __suseconds_t),
]
__fd_mask = c_long
fd_set._fields_ = [
	('fds_bits', __fd_mask * 16),
]

__all__ = ['lseek64', 'lseek',
	'seteuid',
	'isatty', 'execle', 'csync_is_statedb_disabled', 'truncate64',
	'__time_t', 'sleep', 'lockf64',
	'mode_t', '__off64_t', 'size_t', 'csync_walk_local_tree',
	'getegid', 'csync_error_codes_e', 'group_member',
	'get_current_dir_name',
	'csync_update', 'pause', 'csync_set_auth_callback',
	'csync_add_exclude_list', 'getresgid', 'sethostname',
	'fpathconf',
	'__getpgid', 'csync_set_status', 'lchown', 'setgid',
	'getusershell',
	'getlogin',
	'csync_progress_callback', 'intptr_t',
	'csync_walk_remote_tree', 'dup3', 'dup2', 'read',
	'getppid', 'getdomainname',
	'fchown', 'getpgrp',
	'gnu_dev_minor', 'execl', 'readlinkat', 'daemon', 'fsync',
	'csync_set_module_property',
	'tcsetpgrp', 'setreuid', 'csync_destroy',
	'getpagesize', 'setlogin', 'execv', 'nice', 'gnu_dev_makedev', 'ttyname',
	'linkat', 'getlogin_r', '__ssize_t',
	'__confstr_chk',
	'csync_set_config_dir', 'sync',
	'__fd_mask', 'getresuid',
	'fchownat', '__pid_t', 'execlp', 'csync_get_userdata',
	'getgid',
	'__sigset_t',
	'__useconds_t',
	'CSYNC', 'csync_get_config_dir',
	'access',
	'setsid', '__ttyname_r_chk', 'select', 'acct',
	'ualarm',
	'revoke', '__pread64_chk', 'usleep', 'setpgid',
	'setresgid', 'getcwd', 'symlink', 'pwrite64',
	'__getgroups_chk', 'setregid',
	'fchdir', 'ftruncate', 'setegid',
	'vhangup', 'getsid', 'csync_notify_type_e',
	'symlinkat',
	'pipe2', 'sethostid',
	'fd_set',
	'_exit', '__readlink_chk',
	'endusershell', 'confstr', 'csync_treewalk_visit_func',
	'__read_chk', '__mode_t', 'swab', 'csync_get_status',
	'getpgid', 'brk', '__off_t', 'gethostid', 'pread',
	'__readlinkat_chk', 'getdtablesize', 'ttyname_r',
	'__gid_t', 'gethostname', 'timespec',
	'faccessat', 'gnu_dev_major', 'rmdir', 'dup',
	'fdatasync',
	'csync_reconcile', '__pread_chk', 'execvpe',
	'csync_ftw_type_e', 'eaccess', 'execvp', 'ftruncate64',
	'__getlogin_r_chk', 'link', 'uid_t',
	'csync_set_progress_callback', '__getcwd_chk', 'pselect',
	'gid_t', 'execve', 'getpass', 'chdir', '__suseconds_t', 'sbrk',
	'__getwd_chk',
	'csync_get_statedb_file', 'setresuid',
	'csync_auth_callback', 'fexecve', 'vfork', 'setuid',
	'fork', 'csync_enable_conflictcopys', 'lockf', 'sysconf',
	'syscall', 'csync_set_iconv_codec', 'getwd',
	'setdomainname', 'pread64', 'euidaccess', 'close',
	'csync_enable_statedb', 
	'csync_instructions_e', 'time_t', '__gethostname_chk',
	'chroot', 'csync_tree_walk_file_s', 'getgroups',
	'TREE_WALK_FILE', 'ssize_t', 'csync_disable_statedb',
	'setpgrp', 'timeval', 'write', 'csync_get_auth_callback', 'getopt',
	'pathconf',
	'csync_set_userdata', 'truncate', 
	'CSYNC_ERROR_CODE', 'getpid',
	'setusershell', 'readlink', 'unlink',
	'tcgetpgrp', 'unlinkat', '__getdomainname_chk', 'ttyslot',
	'pwrite', 'getuid', 'csync_create', 'alarm',
	'csync_get_local_only', 'csync_init', 'pipe', 'ctermid',
	'chown',
	'csync_set_local_only', '__uid_t', 'profil', 'geteuid']

# vim: noet:ts=4:sw=4:sts=4
