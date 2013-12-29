'''Wrapper for csync0.91.2.h

Generated with:
/home/hefee/.local/bin/ctypesgen.py csync0.91.2.h -o v0_91_2.py --no-macros --exclude csync_version -I .

Do not modify this file.
'''

__docformat__ =  'restructuredtext'
from .preamble import *
from .pre import _lib

__uid_t = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 134

__gid_t = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 135

__mode_t = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 138

__time_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 148

gid_t = __gid_t # /usr/include/unistd.h: 232

uid_t = __uid_t # /usr/include/unistd.h: 237

mode_t = __mode_t # /usr/include/x86_64-linux-gnu/sys/types.h: 70

time_t = __time_t # /usr/include/time.h: 75

enum_csync_status_codes_e = c_int # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_OK = 0 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_ERROR = 1024 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_UNSUCCESSFUL = (CSYNC_STATUS_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_NO_LOCK = (CSYNC_STATUS_UNSUCCESSFUL + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_STATEDB_LOAD_ERROR = (CSYNC_STATUS_NO_LOCK + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_STATEDB_WRITE_ERROR = (CSYNC_STATUS_STATEDB_LOAD_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_NO_MODULE = (CSYNC_STATUS_STATEDB_WRITE_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_TIMESKEW = (CSYNC_STATUS_NO_MODULE + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_FILESYSTEM_UNKNOWN = (CSYNC_STATUS_TIMESKEW + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_TREE_ERROR = (CSYNC_STATUS_FILESYSTEM_UNKNOWN + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_MEMORY_ERROR = (CSYNC_STATUS_TREE_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_PARAM_ERROR = (CSYNC_STATUS_MEMORY_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_UPDATE_ERROR = (CSYNC_STATUS_PARAM_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_RECONCILE_ERROR = (CSYNC_STATUS_UPDATE_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_PROPAGATE_ERROR = (CSYNC_STATUS_RECONCILE_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_REMOTE_ACCESS_ERROR = (CSYNC_STATUS_PROPAGATE_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_REMOTE_CREATE_ERROR = (CSYNC_STATUS_REMOTE_ACCESS_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_REMOTE_STAT_ERROR = (CSYNC_STATUS_REMOTE_CREATE_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_LOCAL_CREATE_ERROR = (CSYNC_STATUS_REMOTE_STAT_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_LOCAL_STAT_ERROR = (CSYNC_STATUS_LOCAL_CREATE_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_PROXY_ERROR = (CSYNC_STATUS_LOCAL_STAT_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_LOOKUP_ERROR = (CSYNC_STATUS_PROXY_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_SERVER_AUTH_ERROR = (CSYNC_STATUS_LOOKUP_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_PROXY_AUTH_ERROR = (CSYNC_STATUS_SERVER_AUTH_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_CONNECT_ERROR = (CSYNC_STATUS_PROXY_AUTH_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_TIMEOUT = (CSYNC_STATUS_CONNECT_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_HTTP_ERROR = (CSYNC_STATUS_TIMEOUT + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_PERMISSION_DENIED = (CSYNC_STATUS_HTTP_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_NOT_FOUND = (CSYNC_STATUS_PERMISSION_DENIED + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_FILE_EXISTS = (CSYNC_STATUS_NOT_FOUND + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_OUT_OF_SPACE = (CSYNC_STATUS_FILE_EXISTS + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_QUOTA_EXCEEDED = (CSYNC_STATUS_OUT_OF_SPACE + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_SERVICE_UNAVAILABLE = (CSYNC_STATUS_QUOTA_EXCEEDED + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_FILE_SIZE_ERROR = (CSYNC_STATUS_SERVICE_UNAVAILABLE + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_CONTEXT_LOST = (CSYNC_STATUS_FILE_SIZE_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_MERGE_FILETREE_ERROR = (CSYNC_STATUS_CONTEXT_LOST + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_CSYNC_STATUS_ERROR = (CSYNC_STATUS_MERGE_FILETREE_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_OPENDIR_ERROR = (CSYNC_STATUS_CSYNC_STATUS_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_READDIR_ERROR = (CSYNC_STATUS_OPENDIR_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_OPEN_ERROR = (CSYNC_STATUS_READDIR_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_ABORTED = (CSYNC_STATUS_OPEN_ERROR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_INDIVIDUAL_IS_SYMLINK = (CSYNC_STATUS_ABORTED + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_INDIVIDUAL_IGNORE_LIST = (CSYNC_STATUS_INDIVIDUAL_IS_SYMLINK + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS_INDIVIDUAL_IS_INVALID_CHARS = (CSYNC_STATUS_INDIVIDUAL_IGNORE_LIST + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 59

CSYNC_STATUS = enum_csync_status_codes_e # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 109

enum_csync_instructions_e = c_int # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_NONE = 0 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_EVAL = 1 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_REMOVE = 2 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_RENAME = 4 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_EVAL_RENAME = 2048 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_NEW = 8 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_CONFLICT = 16 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_IGNORE = 32 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_SYNC = 64 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_STAT_ERROR = 128 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_ERROR = 256 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_DELETED = 512 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

CSYNC_INSTRUCTION_UPDATED = 1024 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 123

enum_csync_ftw_type_e = c_int # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 140

CSYNC_FTW_TYPE_FILE = 0 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 140

CSYNC_FTW_TYPE_SLINK = (CSYNC_FTW_TYPE_FILE + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 140

CSYNC_FTW_TYPE_DIR = (CSYNC_FTW_TYPE_SLINK + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 140

CSYNC_FTW_TYPE_SKIP = (CSYNC_FTW_TYPE_DIR + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 140

enum_csync_notify_type_e = c_int # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_INVALID = 0 # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_START_SYNC_SEQUENCE = (CSYNC_NOTIFY_INVALID + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_START_DOWNLOAD = (CSYNC_NOTIFY_START_SYNC_SEQUENCE + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_START_UPLOAD = (CSYNC_NOTIFY_START_DOWNLOAD + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_PROGRESS = (CSYNC_NOTIFY_START_UPLOAD + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_FINISHED_DOWNLOAD = (CSYNC_NOTIFY_PROGRESS + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_FINISHED_UPLOAD = (CSYNC_NOTIFY_FINISHED_DOWNLOAD + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_FINISHED_SYNC_SEQUENCE = (CSYNC_NOTIFY_FINISHED_UPLOAD + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_START_DELETE = (CSYNC_NOTIFY_FINISHED_SYNC_SEQUENCE + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_END_DELETE = (CSYNC_NOTIFY_START_DELETE + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

CSYNC_NOTIFY_ERROR = (CSYNC_NOTIFY_END_DELETE + 1) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 147

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 161
class struct_csync_progress_s(Structure):
    pass

struct_csync_progress_s.__slots__ = [
    'kind',
    'path',
    'curr_bytes',
    'file_size',
    'overall_transmission_size',
    'current_overall_bytes',
    'overall_file_count',
    'current_file_no',
]

struct_csync_progress_s._fields_ = [
    ('kind', enum_csync_notify_type_e),
    ('path', String),
    ('curr_bytes', c_int64),
    ('file_size', c_int64),
    ('overall_transmission_size', c_int64),
    ('current_overall_bytes', c_int64),
    ('overall_file_count', c_int64),
    ('current_file_no', c_int64),
]

CSYNC_PROGRESS = struct_csync_progress_s # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 176

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 186
class struct_csync_tree_walk_file_s(Structure):
    pass

struct_csync_tree_walk_file_s.__slots__ = [
    'path',
    'size',
    'modtime',
    'uid',
    'gid',
    'mode',
    'type',
    'instruction',
    'should_update_etag',
    'rename_path',
    'etag',
    'file_id',
    'error_status',
]
struct_csync_tree_walk_file_s._fields_ = [
    ('path', String),
    ('size', c_int64),
    ('modtime', time_t),
    ('uid', uid_t),
    ('gid', gid_t),
    ('mode', mode_t),
    ('type', enum_csync_ftw_type_e),
    ('instruction', enum_csync_instructions_e),
    ('should_update_etag', c_int),
    ('rename_path', String),
    ('etag', String),
    ('file_id', String),
    ('error_status', CSYNC_STATUS),
]

TREE_WALK_FILE = struct_csync_tree_walk_file_s # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 209

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 214
class struct_csync_s(Structure):
    pass

CSYNC = struct_csync_s # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 214

csync_auth_callback = CFUNCTYPE(c_int, String, c_void_p, c_size_t, c_int, c_int, c_void_p) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 216

csync_log_callback = CFUNCTYPE(UNCHECKED(None), c_int, String, String, POINTER(None)) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 219

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 231
if hasattr(_lib, 'csync_status_ok'):
    csync_status_ok = _lib.csync_status_ok
    csync_status_ok.argtypes = [POINTER(CSYNC)]
    csync_status_ok.restype = c_uint8


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 240
if hasattr(_lib, 'csync_create'):
    csync_create = _lib.csync_create
    csync_create.argtypes = [POINTER(POINTER(CSYNC)), c_char_p, c_char_p]
    csync_create.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 251
if hasattr(_lib, 'csync_init'):
    csync_init = _lib.csync_init
    csync_init.argtypes = [POINTER(CSYNC)]
    csync_init.restype = c_int

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 260
if hasattr(_lib, 'csync_update'):
    csync_update = _lib.csync_update
    csync_update.argtypes = [POINTER(CSYNC)]
    csync_update.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 269
if hasattr(_lib, 'csync_reconcile'):
    csync_reconcile = _lib.csync_reconcile
    csync_reconcile.argtypes = [POINTER(CSYNC)]
    csync_reconcile.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 278
if hasattr(_lib, 'csync_propagate'):
    csync_propagate = _lib.csync_propagate
    csync_propagate.argtypes = [POINTER(CSYNC)]
    csync_propagate.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 287
if hasattr(_lib, 'csync_commit'):
    csync_commit = _lib.csync_commit
    csync_commit.argtypes = [POINTER(CSYNC)]
    csync_commit.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 298
if hasattr(_lib, 'csync_destroy'):
    csync_destroy = _lib.csync_destroy
    csync_destroy.argtypes = [POINTER(CSYNC)]
    csync_destroy.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 334
if hasattr(_lib, 'csync_add_exclude_list'):
    csync_add_exclude_list = _lib.csync_add_exclude_list
    csync_add_exclude_list.argtypes = [POINTER(CSYNC), String]
    csync_add_exclude_list.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 341
if hasattr(_lib, 'csync_clear_exclude_list'):
    csync_clear_exclude_list = _lib.csync_clear_exclude_list
    csync_clear_exclude_list.argtypes = [POINTER(CSYNC)]
    csync_clear_exclude_list.restype = None


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 350
if hasattr(_lib, 'csync_get_config_dir'):
    csync_get_config_dir = _lib.csync_get_config_dir
    csync_get_config_dir.argtypes = [POINTER(CSYNC)]
    if sizeof(c_int) == sizeof(c_void_p):
        csync_get_config_dir.restype = ReturnString
    else:
        csync_get_config_dir.restype = String
        csync_get_config_dir.errcheck = ReturnString


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 361
if hasattr(_lib, 'csync_set_config_dir'):
    csync_set_config_dir = _lib.csync_set_config_dir
    csync_set_config_dir.argtypes = [POINTER(CSYNC), String]
    csync_set_config_dir.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 370
if hasattr(_lib, 'csync_remove_config_dir'):
    csync_remove_config_dir = _lib.csync_remove_config_dir
    csync_remove_config_dir.argtypes = [POINTER(CSYNC)]
    csync_remove_config_dir.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 379
if hasattr(_lib, 'csync_enable_statedb'):
    csync_enable_statedb = _lib.csync_enable_statedb
    csync_enable_statedb.argtypes = [POINTER(CSYNC)]
    csync_enable_statedb.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 388
if hasattr(_lib, 'csync_disable_statedb'):
    csync_disable_statedb = _lib.csync_disable_statedb
    csync_disable_statedb.argtypes = [POINTER(CSYNC)]
    csync_disable_statedb.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 397
if hasattr(_lib, 'csync_is_statedb_disabled'):
    csync_is_statedb_disabled = _lib.csync_is_statedb_disabled
    csync_is_statedb_disabled.argtypes = [POINTER(CSYNC)]
    csync_is_statedb_disabled.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 407
if hasattr(_lib, 'csync_get_userdata'):
    csync_get_userdata = _lib.csync_get_userdata
    csync_get_userdata.argtypes = [POINTER(CSYNC)]
    csync_get_userdata.restype = POINTER(None)


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 419
if hasattr(_lib, 'csync_set_userdata'):
    csync_set_userdata = _lib.csync_set_userdata
    csync_set_userdata.argtypes = [POINTER(CSYNC), POINTER(None)]
    csync_set_userdata.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 429
if hasattr(_lib, 'csync_get_auth_callback'):
    csync_get_auth_callback = _lib.csync_get_auth_callback
    csync_get_auth_callback.argtypes = [POINTER(CSYNC)]
    csync_get_auth_callback.restype = csync_auth_callback


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 440
if hasattr(_lib, 'csync_set_auth_callback'):
    csync_set_auth_callback = _lib.csync_set_auth_callback
    csync_set_auth_callback.argtypes = [POINTER(CSYNC), csync_auth_callback]
    csync_set_auth_callback.restype = c_int

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 449
if hasattr(_lib, 'csync_set_log_level'):
    csync_set_log_level = _lib.csync_set_log_level
    csync_set_log_level.argtypes = [c_int]
    csync_set_log_level.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 456
if hasattr(_lib, 'csync_get_log_level'):
    csync_get_log_level = _lib.csync_get_log_level
    csync_get_log_level.argtypes = []
    csync_get_log_level.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 464
if hasattr(_lib, 'csync_get_log_callback'):
    csync_get_log_callback = _lib.csync_get_log_callback
    csync_get_log_callback.argtypes = []
    csync_get_log_callback.restype = csync_log_callback


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 473
if hasattr(_lib, 'csync_set_log_callback'):
    csync_set_log_callback = _lib.csync_set_log_callback
    csync_set_log_callback.argtypes = [csync_log_callback]
    csync_set_log_callback.restype = c_int

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 480
if hasattr(_lib, 'csync_get_log_userdata'):
    csync_get_log_userdata = _lib.csync_get_log_userdata
    csync_get_log_userdata.argtypes = []
    csync_get_log_userdata.restype = POINTER(None)


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 489
if hasattr(_lib, 'csync_set_log_userdata'):
    csync_set_log_userdata = _lib.csync_set_log_userdata
    csync_set_log_userdata.argtypes = [POINTER(None)]
    csync_set_log_userdata.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 498
if hasattr(_lib, 'csync_get_statedb_file'):
    csync_get_statedb_file = _lib.csync_get_statedb_file
    csync_get_statedb_file.argtypes = [POINTER(CSYNC)]
    if sizeof(c_int) == sizeof(c_void_p):
        csync_get_statedb_file.restype = ReturnString
    else:
        csync_get_statedb_file.restype = String
        csync_get_statedb_file.errcheck = ReturnString


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 507
if hasattr(_lib, 'csync_enable_conflictcopys'):
    csync_enable_conflictcopys = _lib.csync_enable_conflictcopys
    csync_enable_conflictcopys.argtypes = [POINTER(CSYNC)]
    csync_enable_conflictcopys.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 516
if hasattr(_lib, 'csync_set_local_only'):
    csync_set_local_only = _lib.csync_set_local_only
    csync_set_local_only.argtypes = [POINTER(CSYNC), c_uint8]
    csync_set_local_only.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 523
if hasattr(_lib, 'csync_get_local_only'):
    csync_get_local_only = _lib.csync_get_local_only
    csync_get_local_only.argtypes = [POINTER(CSYNC)]
    csync_get_local_only.restype = c_uint8

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 526
if hasattr(_lib, 'csync_get_status'):
    csync_get_status = _lib.csync_get_status
    csync_get_status.argtypes = [POINTER(CSYNC)]
    csync_get_status.restype = CSYNC_STATUS


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 529
if hasattr(_lib, 'csync_set_status'):
    csync_set_status = _lib.csync_set_status
    csync_set_status.argtypes = [POINTER(CSYNC), c_int]
    csync_set_status.restype = c_int

csync_treewalk_visit_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(TREE_WALK_FILE), POINTER(None)) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 531

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 542
if hasattr(_lib, 'csync_walk_local_tree'):
    csync_walk_local_tree = _lib.csync_walk_local_tree
    csync_walk_local_tree.argtypes = [POINTER(CSYNC), POINTER(csync_treewalk_visit_func), c_int]
    csync_walk_local_tree.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 553
if hasattr(_lib, 'csync_walk_remote_tree'):
    csync_walk_remote_tree = _lib.csync_walk_remote_tree
    csync_walk_remote_tree.argtypes = [POINTER(CSYNC), POINTER(csync_treewalk_visit_func), c_int]
    csync_walk_remote_tree.restype = c_int

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 562
if hasattr(_lib, 'csync_get_status_string'):
    csync_get_status_string = _lib.csync_get_status_string
    csync_get_status_string.argtypes = [POINTER(CSYNC)]
    if sizeof(c_int) == sizeof(c_void_p):
        csync_get_status_string.restype = ReturnString
    else:
        csync_get_status_string.restype = String
        csync_get_status_string.errcheck = ReturnString

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 586
if hasattr(_lib, 'csync_set_module_property'):
    csync_set_module_property = _lib.csync_set_module_property
    csync_set_module_property.argtypes = [POINTER(CSYNC), String, POINTER(None)]
    csync_set_module_property.restype = c_int


csync_progress_callback = CFUNCTYPE(UNCHECKED(None), POINTER(CSYNC_PROGRESS), POINTER(None)) # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 595

# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 603
if hasattr(_lib, 'csync_set_progress_callback'):
    csync_set_progress_callback = _lib.csync_set_progress_callback
    csync_set_progress_callback.argtypes = [POINTER(CSYNC), csync_progress_callback]
    csync_set_progress_callback.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 605
if hasattr(_lib, 'csync_get_progress_callback'):
    csync_get_progress_callback = _lib.csync_get_progress_callback
    csync_get_progress_callback.argtypes = [POINTER(CSYNC)]
    csync_get_progress_callback.restype = csync_progress_callback


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 612
if hasattr(_lib, 'csync_request_abort'):
    csync_request_abort = _lib.csync_request_abort
    csync_request_abort.argtypes = [POINTER(CSYNC)]
    csync_request_abort.restype = None


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 619
if hasattr(_lib, 'csync_resume'):
    csync_resume = _lib.csync_resume
    csync_resume.argtypes = [POINTER(CSYNC)]
    csync_resume.restype = None


# /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 626
if hasattr(_lib, 'csync_abort_requested'):
    csync_abort_requested = _lib.csync_abort_requested
    csync_abort_requested.argtypes = [POINTER(CSYNC)]
    csync_abort_requested.restype = c_int


csync_progress_s = struct_csync_progress_s # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 161

csync_tree_walk_file_s = struct_csync_tree_walk_file_s # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 186

csync_s = struct_csync_s # /home/hefee/hg/pyOwnCloud/csync0.91.2.h: 214

# No inserted files
