import ctypes
from ctypes import (
	c_bool, c_char_p, c_size_t, c_void_p,
	c_byte, c_char, c_short, c_int, c_long, c_longlong,
	c_ubyte, c_ushort, c_uint, c_ulong, c_ulonglong,
	c_int8, c_int16, c_int32, c_int64,
	c_uint8, c_uint16, c_uint32, c_uint64,
	addressof, pointer, cast as reinterpret_cast, sizeof,
)

NULL = 0

def __EQ__(self, other):
	if type(self) is type(other):
		return self.value == other.value
	_root = {
		1: c_uint8,
		2: c_uint16,
		4: c_uint32,
		8: c_uint64,
	}
	if isinstance(other, ctypes._SimpleCData):
		return _root[sizeof(self)].from_address(addressof(self)).value == _root[sizeof(other)].from_address(addressof(other)).value
	if isinstance(other, (bool, type(None))):
		other = 1 if other else 0
	if isinstance(other, (int, long)):
		return __EQ__(self, type(self)(other))
	return False

__NE__ = lambda self, other: not(__EQ__(self, other))

map(lambda x: (setattr(x, '__eq__', __EQ__), setattr(x, '__ne__', __NE__)), [
	c_bool, c_byte, c_char, c_ubyte,
	c_int8, c_int16, c_int32, c_int64,
	c_uint8, c_uint16, c_uint32, c_uint64,
])

class _STRUCT(ctypes.Structure):
	def __eq__(self, other):
		if self._fields_ != other._fields_:
			return False
		for (name, T) in self._fields_:
			if getattr(self, name) != getattr(other, name):
				return False
		return True

	def __nonzero__(self):
		return any(map(lambda x: getattr(self, x[0]), self._fields_))

	def __ne__(self, other):
		return not self == other

	def __repr__(self):
		return self.__class__.__name__ + '{' + ', '.join(map(lambda x: x[0] + ': ' + repr(self.__getattribute__(x[0])), self._fields_)) + '}'

class _UNION(ctypes.Union):
	def __eq__(self, other):
		if self._fields_ != other._fields_:
			return False
		for (name, T) in self._fields_:
			if getattr(self, name) != getattr(other, name):
				return False
		return True

	def __nonzero__(self):
		return any(map(lambda x: getattr(self, x[0]), self._fields_))

	def __ne__(self, other):
		return not self == other

class __ENUM(type(c_uint)):
	def __init__(cls, name, bases, dct):
		type.__init__(cls, name, bases, dct)
		if '_traits_' in dct:
			index = 0
			_traits_ = {}
			for item in dct['_traits_']:
				if isinstance(item, (list, tuple)):
					item, index = item[0], item[1]
				setattr(cls, item, cls(index))
				_traits_[index] = item
				index += 1
			cls._traits_ = _traits_

class _ENUM(c_uint, metaclass = __ENUM):
	def __init__(self, value = 0):
		if isinstance(value, _ENUM):
			value = value.value
		c_uint.__init__(self, value)

	def __str__(self):
		retval = str(self.value)
		if self.value in self.__class__._traits_:
			retval += ' (' + self.__class__.__name__ + '.' + self.__class__._traits_[self.value]  + ')'
		return retval


# VMware Virtual Disk Library
VIXDISKLIB_VERSION_MAJOR = 1
VIXDISKLIB_VERSION_MINOR = 0

VIXDISKLIB_SECTOR_SIZE = 512

VIXDISKLIB_HWVERSION_WORKSTATION_4 = 3
VIXDISKLIB_HWVERSION_WORKSTATION_5 = 4
VIXDISKLIB_HWVERSION_ESX30 = VIXDISKLIB_HWVERSION_WORKSTATION_5
VIXDISKLIB_HWVERSION_WORKSTATION_6 = 6
VIXDISKLIB_HWVERSION_CURRENT = VIXDISKLIB_HWVERSION_WORKSTATION_6

VIXDISKLIB_FLAG_OPEN_UNBUFFERED = 1 << 0
VIXDISKLIB_FLAG_OPEN_SINGLE_LINK = 1 << 1
VIXDISKLIB_FLAG_OPEN_READ_ONLY = 1 << 2

VIX_OK = 0
VIX_E_FAIL = 1
VIX_E_OUT_OF_MEMORY = 2
VIX_E_INVALID_ARG = 3
VIX_E_FILE_NOT_FOUND = 4
VIX_E_OBJECT_IS_BUSY = 5
VIX_E_NOT_SUPPORTED = 6
VIX_E_FILE_ERROR = 7
VIX_E_DISK_FULL = 8
VIX_E_INCORRECT_FILE_TYPE = 9
VIX_E_CANCELLED = 10
VIX_E_FILE_READ_ONLY = 11
VIX_E_FILE_ALREADY_EXISTS = 12
VIX_E_FILE_ACCESS_ERROR = 13
VIX_E_REQUIRES_LARGE_FILES = 14
VIX_E_FILE_ALREADY_LOCKED = 15
VIX_E_NOT_SUPPORTED_ON_REMOTE_OBJECT = 20
VIX_E_FILE_TOO_BIG = 21
VIX_E_FILE_NAME_INVALID = 22
VIX_E_ALREADY_EXISTS = 23
VIX_E_BUFFER_TOOSMALL = 24
VIX_E_INVALID_HANDLE = 1000
VIX_E_NOT_SUPPORTED_ON_HANDLE_TYPE = 1001
VIX_E_TOO_MANY_HANDLES = 1002
VIX_E_NOT_FOUND = 2000
VIX_E_TYPE_MISMATCH = 2001
VIX_E_INVALID_XML = 2002
VIX_E_TIMEOUT_WAITING_FOR_TOOLS = 3000
VIX_E_UNRECOGNIZED_COMMAND = 3001
VIX_E_OP_NOT_SUPPORTED_ON_GUEST = 3003
VIX_E_PROGRAM_NOT_STARTED = 3004
VIX_E_CANNOT_START_READ_ONLY_VM = 3005
VIX_E_VM_NOT_RUNNING = 3006
VIX_E_VM_IS_RUNNING = 3007
VIX_E_CANNOT_CONNECT_TO_VM = 3008
VIX_E_POWEROP_SCRIPTS_NOT_AVAILABLE = 3009
VIX_E_NO_GUEST_OS_INSTALLED = 3010
VIX_E_VM_INSUFFICIENT_HOST_MEMORY = 3011
VIX_E_SUSPEND_ERROR = 3012
VIX_E_VM_NOT_ENOUGH_CPUS = 3013
VIX_E_HOST_USER_PERMISSIONS = 3014
VIX_E_GUEST_USER_PERMISSIONS = 3015
VIX_E_TOOLS_NOT_RUNNING = 3016
VIX_E_GUEST_OPERATIONS_PROHIBITED = 3017
VIX_E_ANON_GUEST_OPERATIONS_PROHIBITED = 3018
VIX_E_ROOT_GUEST_OPERATIONS_PROHIBITED = 3019
VIX_E_MISSING_ANON_GUEST_ACCOUNT = 3023
VIX_E_CANNOT_AUTHENTICATE_WITH_GUEST = 3024
VIX_E_UNRECOGNIZED_COMMAND_IN_GUEST = 3025
VIX_E_CONSOLE_GUEST_OPERATIONS_PROHIBITED = 3026
VIX_E_MUST_BE_CONSOLE_USER = 3027
VIX_E_NOT_ALLOWED_DURING_VM_RECORDING = 3028
VIX_E_NOT_ALLOWED_DURING_VM_REPLAY = 3029
VIX_E_VM_NOT_FOUND = 4000
VIX_E_NOT_SUPPORTED_FOR_VM_VERSION = 4001
VIX_E_CANNOT_READ_VM_CONFIG = 4002
VIX_E_TEMPLATE_VM = 4003
VIX_E_VM_ALREADY_LOADED = 4004
VIX_E_VM_ALREADY_UP_TO_DATE = 4006
VIX_E_UNRECOGNIZED_PROPERTY = 6000
VIX_E_INVALID_PROPERTY_VALUE = 6001
VIX_E_READ_ONLY_PROPERTY = 6002
VIX_E_MISSING_REQUIRED_PROPERTY = 6003
VIX_E_BAD_VM_INDEX = 8000
VIX_E_SNAPSHOT_INVAL = 13000
VIX_E_SNAPSHOT_DUMPER = 13001
VIX_E_SNAPSHOT_DISKLIB = 13002
VIX_E_SNAPSHOT_NOTFOUND = 13003
VIX_E_SNAPSHOT_EXISTS = 13004
VIX_E_SNAPSHOT_VERSION = 13005
VIX_E_SNAPSHOT_NOPERM = 13006
VIX_E_SNAPSHOT_CONFIG = 13007
VIX_E_SNAPSHOT_NOCHANGE = 13008
VIX_E_SNAPSHOT_CHECKPOINT = 13009
VIX_E_SNAPSHOT_LOCKED = 13010
VIX_E_SNAPSHOT_INCONSISTENT = 13011
VIX_E_SNAPSHOT_NAMETOOLONG = 13012
VIX_E_SNAPSHOT_VIXFILE = 13013
VIX_E_SNAPSHOT_DISKLOCKED = 13014
VIX_E_SNAPSHOT_DUPLICATEDDISK = 13015
VIX_E_SNAPSHOT_INDEPENDENTDISK = 13016
VIX_E_SNAPSHOT_NONUNIQUE_NAME = 13017
VIX_E_HOST_DISK_INVALID_VALUE = 14003
VIX_E_HOST_DISK_SECTORSIZE = 14004
VIX_E_HOST_FILE_ERROR_EOF = 14005
VIX_E_HOST_NETBLKDEV_HANDSHAKE = 14006
VIX_E_HOST_SOCKET_CREATION_ERROR = 14007
VIX_E_HOST_SERVER_NOT_FOUND = 14008
VIX_E_HOST_NETWORK_CONN_REFUSED = 14009
VIX_E_HOST_TCP_SOCKET_ERROR = 14010
VIX_E_HOST_TCP_CONN_LOST = 14011
VIX_E_HOST_NBD_HASHFILE_VOLUME = 14012
VIX_E_HOST_NBD_HASHFILE_INIT = 14013
VIX_E_DISK_INVAL = 16000
VIX_E_DISK_NOINIT = 16001
VIX_E_DISK_NOIO = 16002
VIX_E_DISK_PARTIALCHAIN = 16003
VIX_E_DISK_NEEDSREPAIR = 16006
VIX_E_DISK_OUTOFRANGE = 16007
VIX_E_DISK_CID_MISMATCH = 16008
VIX_E_DISK_CANTSHRINK = 16009
VIX_E_DISK_PARTMISMATCH = 16010
VIX_E_DISK_UNSUPPORTEDDISKVERSION = 16011
VIX_E_DISK_OPENPARENT = 16012
VIX_E_DISK_NOTSUPPORTED = 16013
VIX_E_DISK_NEEDKEY = 16014
VIX_E_DISK_NOKEYOVERRIDE = 16015
VIX_E_DISK_NOTENCRYPTED = 16016
VIX_E_DISK_NOKEY = 16017
VIX_E_DISK_INVALIDPARTITIONTABLE = 16018
VIX_E_DISK_NOTNORMAL = 16019
VIX_E_DISK_NOTENCDESC = 16020
VIX_E_DISK_NEEDVMFS = 16022
VIX_E_DISK_RAWTOOBIG = 16024
VIX_E_DISK_TOOMANYOPENFILES = 16027
VIX_E_DISK_TOOMANYREDO = 16028
VIX_E_DISK_RAWTOOSMALL = 16029
VIX_E_DISK_INVALIDCHAIN = 16030
VIX_E_DISK_KEY_NOTFOUND = 16052
VIX_E_DISK_SUBSYSTEM_INIT_FAIL = 16053
VIX_E_DISK_INVALID_CONNECTION = 16054
VIX_E_DISK_NOLICENSE = 16064
VIX_E_CANNOT_CONNECT_TO_HOST = 18000
VIX_E_NOT_FOR_REMOTE_HOST = 18001
VIX_E_NOT_A_FILE = 20001
VIX_E_NOT_A_DIRECTORY = 20002
VIX_E_NO_SUCH_PROCESS = 20003
VIX_E_FILE_NAME_TOO_LONG = 20004


VmTimeType = c_int64
VmTimeRealClock = c_int64
VmTimeVirtualClock = c_int64
VixError = c_uint64
VixDiskLibSectorType = c_uint64
VIX_ERROR_CODE = lambda err: err & 0xFFFF
VIX_SUCCEEDED = lambda err: VIX_OK == err
VIX_FAILED = lambda err: VIX_OK != err

class VixDiskLibException(Exception):
	pass

def _VIXDISKLIB_CHECKED(vixError):
	if VIX_SUCCEEDED(vixError):
		return vixError
	raise VixDiskLibException(PyVixDiskLib_GetErrorText(vixError))

class _VIX_STRUCT(_STRUCT):
	_pack_ = 4

class _VIX_UNION(_UNION):
	_pack_ = 4

class VixDiskLibGeometry(_VIX_STRUCT):
	_fields_ = [
		('cylinders', c_uint32),
		('heads', c_uint32),
		('sectors', c_uint32),
	]

class VixDiskLibDiskType(_ENUM):
	_traits_ = [
		('VIXDISKLIB_DISK_MONOLITHIC_SPARSE', 1),
		'VIXDISKLIB_DISK_MONOLITHIC_FLAT',
		'VIXDISKLIB_DISK_SPLIT_SPARSE',
		'VIXDISKLIB_DISK_SPLIT_FLAT',
		'VIXDISKLIB_DISK_VMFS_FLAT',
		'VIXDISKLIB_DISK_STREAM_OPTIMIZED',
		('VIXDISKLIB_DISK_UNKNOWN', 256),
	]

class VixDiskLibAdapterType(_ENUM):
	_traits_ = [
		('VIXDISKLIB_ADAPTER_IDE', 1),
		'VIXDISKLIB_ADAPTER_SCSI_BUSLOGIC',
		'VIXDISKLIB_ADAPTER_SCSI_LSILOGIC',
		('VIXDISKLIB_ADAPTER_UNKNOWN', 256),
	]

class VixDiskLibCreateParams(_VIX_STRUCT):
	_fields_ = [
		('diskType', VixDiskLibDiskType),
		('adapterType', VixDiskLibAdapterType),
		('hwVersion', c_uint16),
		('capacity', VixDiskLibSectorType),
	]
LPVixDiskLibCreateParams = ctypes.POINTER(VixDiskLibCreateParams)

class VixDiskLibCredType(_ENUM):
	_traits_ = [
		('VIXDISKLIB_CRED_UID', 1),
		'VIXDISKLIB_CRED_SESSIONID',
		'VIXDISKLIB_CRED_TICKETID',
		('VIXDISKLIB_CRED_UNKNOWN', 256),
	]

class VixDiskLibConnectParams(_VIX_STRUCT):
	class VixDiskLibCreds(_VIX_UNION):
		class VixDiskLibUidPasswdCreds(_VIX_STRUCT):
			_fields_ = [
				('userName', c_char_p),
				('password', c_char_p),
			]
		class VixDiskLibSessionIdCreds(_VIX_STRUCT):
			_fields_ = [
				('cookie', c_char_p),
				('userName', c_char_p),
				('key', c_char_p),
			]
		_fields_ = [
			('uid', VixDiskLibUidPasswdCreds),
			('sessionId', VixDiskLibSessionIdCreds),
			('ticketId', c_void_p), # ctypes.POINTER(VixDiskLibTicketIdCreds)
		]
	_fields_ = [
		('vmxSpec', c_char_p),
		('serverName', c_char_p),
		('credType', VixDiskLibCredType),
		('creds', VixDiskLibCreds),
		('port', c_uint32),
	]
LPVixDiskLibConnectParams = ctypes.POINTER(VixDiskLibConnectParams)

class VixDiskLibInfo(_VIX_STRUCT):
	_fields_ = [
		('biosGeo', VixDiskLibGeometry),
		('physGeo', VixDiskLibGeometry),
		('capacity', VixDiskLibSectorType),
		('adapterType', VixDiskLibAdapterType),
		('numLinks', c_int),
		('parentFileNameHint', c_char_p),
	]
LPVixDiskLibInfo = ctypes.POINTER(VixDiskLibInfo)

class VixDiskLibConnectParam(_VIX_STRUCT):
	pass # declared without definition
VixDiskLibConnection = ctypes.POINTER(VixDiskLibConnectParam)

class VixDiskLibHandleStruct(_VIX_STRUCT):
	pass # declared without definition
VixDiskLibHandle = ctypes.POINTER(VixDiskLibHandleStruct)
LPVixDiskLibHandle = ctypes.POINTER(VixDiskLibHandle)

VixDiskLibProgressFunc = ctypes.CFUNCTYPE(c_bool, c_void_p, c_int)
_PyDefaultVixDiskLibProgressFunc = VixDiskLibProgressFunc(NULL)

_IMPORT = [
	['VixDiskLib_Attach', VixError, VixDiskLibHandle, VixDiskLibHandle],
	['VixDiskLib_Clone', VixError, VixDiskLibConnection, c_char_p, VixDiskLibConnection, c_char_p, LPVixDiskLibCreateParams, VixDiskLibProgressFunc, c_void_p, c_bool],
	['VixDiskLib_Close', VixError, VixDiskLibHandle],
	['VixDiskLib_Connect', VixError, LPVixDiskLibConnectParams, ctypes.POINTER(VixDiskLibConnection)],
	['VixDiskLib_Create', VixError, VixDiskLibConnection, c_char_p, LPVixDiskLibCreateParams, VixDiskLibProgressFunc, c_void_p],
	['VixDiskLib_CreateChild', VixError, VixDiskLibHandle, c_char_p, VixDiskLibDiskType, VixDiskLibProgressFunc, c_void_p],
	['VixDiskLib_Defragment', VixError, VixDiskLibHandle, VixDiskLibProgressFunc, c_void_p],
	['VixDiskLib_Disconnect', VixError, VixDiskLibConnection],
	['VixDiskLib_Exit'],
	['VixDiskLib_FreeInfo', None, LPVixDiskLibInfo],
	['VixDiskLib_GetErrorText', c_void_p, VixError, c_char_p],
	['VixDiskLib_GetInfo', VixError, VixDiskLibHandle, ctypes.POINTER(LPVixDiskLibInfo)],
	['VixDiskLib_GetMetadataKeys', VixError, VixDiskLibHandle, c_char_p, c_size_t, ctypes.POINTER(c_size_t)],
	['VixDiskLib_Grow', VixError, VixDiskLibConnection, c_char_p, VixDiskLibSectorType, c_bool, VixDiskLibProgressFunc, c_void_p],
	['VixDiskLib_FreeErrorText', None, c_void_p],
	['VixDiskLib_Init', VixError, c_uint32, c_uint32, c_void_p, c_void_p, c_void_p, c_void_p],
	['VixDiskLib_Open', VixError, VixDiskLibConnection, c_char_p, c_uint32, LPVixDiskLibHandle],
	['VixDiskLib_Read', VixError, VixDiskLibHandle, VixDiskLibSectorType, VixDiskLibSectorType, c_char_p],
	['VixDiskLib_ReadMetadata', VixError, VixDiskLibHandle, c_char_p, c_char_p, c_size_t, ctypes.POINTER(c_size_t)],
	['VixDiskLib_Rename', c_char_p, c_char_p],
	['VixDiskLib_Shrink', VixError, VixDiskLibHandle, VixDiskLibProgressFunc, c_void_p],
	['VixDiskLib_SpaceNeededForClone', VixError, VixDiskLibHandle, VixDiskLibDiskType, ctypes.POINTER(c_uint64)],
	['VixDiskLib_Unlink', VixError, VixDiskLibConnection, c_char_p],
	['VixDiskLib_Write', VixError, VixDiskLibHandle, VixDiskLibSectorType, VixDiskLibSectorType, c_char_p],
	['VixDiskLib_WriteMetadata', VixError, c_char_p, c_char_p],
]

try:
	vixDiskLib = None
	import platform
	if platform.system() == 'Windows':
		ctypes.windll.kernel32.SetDllDirectoryW(r'C:\Program Files\VMware\VMware Virtual Disk Development Kit\bin')
		vixDiskLib = ctypes.CDLL('vixDiskLib')
	elif platform.system() == 'Linux':
		vixDiskLib = ctypes.CDLL('/usr/lib/vmware-vix-disklib/lib32/libvixDiskLib.so')
	for entry in _IMPORT:
		thunk = vixDiskLib[entry[0]]
		thunk.restype = entry[1] if len(entry) >= 2 else None
		thunk.argtypes = entry[2:]
		globals()[entry[0]] = thunk
except:
	pass

class PyLPVixDiskLibInfo(LPVixDiskLibInfo):
	_type_ = VixDiskLibInfo
	def __del__(self):
		VixDiskLib_FreeInfo(self)

class PyVixDiskLibConnection(VixDiskLibConnection):
	_type_ = VixDiskLibConnectParam
	def __del__(self):
		VixDiskLib_Disconnect(self)

class PyVixDiskLibHandle(VixDiskLibHandle):
	_type_ = VixDiskLibHandleStruct
	def __del__(self):
		VixDiskLib_Close(self)

def PyVixDiskLib_Create(connection, path, createParams, progressFunc = None, *params):
	@VixDiskLibProgressFunc
	def thunk(progressCallbackData, progress):
		return bool(progressFunc(progress, *params))
	_VIXDISKLIB_CHECKED(VixDiskLib_Create(connection, path, createParams, _PyDefaultVixDiskLibProgressFunc if progressFunc is None else thunk, NULL))

def PyVixDiskLib_CreateChild(diskHandle, childPath, diskType = VixDiskLibDiskType.VIXDISKLIB_DISK_MONOLITHIC_SPARSE, progressFunc = None, *params):
	@VixDiskLibProgressFunc
	def thunk(progressCallbackData, progress):
		return bool(progressFunc(progress, *params))
	_VIXDISKLIB_CHECKED(VixDiskLib_CreateChild(diskHandle, childPath, diskType, _PyDefaultVixDiskLibProgressFunc if progressFunc is None else thunk, NULL))

def PyVixDiskLib_Connect(connectParams = reinterpret_cast(NULL, LPVixDiskLibConnectParams)):
	retval = PyVixDiskLibConnection()
	_VIXDISKLIB_CHECKED(VixDiskLib_Connect(connectParams, pointer(retval)))
	return retval

def PyVixDiskLib_Defragment(diskHandle, progressFunc = None, *params):
	@VixDiskLibProgressFunc
	def thunk(progressCallbackData, progress):
		return bool(progressFunc(progress, *params))
	_VIXDISKLIB_CHECKED(VixDiskLib_Defragment(diskHandle, _PyDefaultVixDiskLibProgressFunc if progressFunc is None else thunk, NULL))

def PyVixDiskLib_GetErrorText(err, locale = c_char_p(NULL)):
	errMsg = VixDiskLib_GetErrorText(err, locale)
	retval = reinterpret_cast(errMsg, c_char_p).value
	VixDiskLib_FreeErrorText(errMsg)
	return retval

def PyVixDiskLib_GetInfo(diskHandle):
	retval = PyLPVixDiskLibInfo()
	_VIXDISKLIB_CHECKED(VixDiskLib_GetInfo(diskHandle, ctypes.pointer(retval)))
	return retval.contents

def PyVixDiskLib_GetMetadataKeys(diskHandle):
	bufsize = c_size_t()
	VixDiskLib_GetMetadataKeys(diskHandle, c_char_p(0), 0, pointer(bufsize))
	buf = ctypes.create_string_buffer(bufsize.value)
	_VIXDISKLIB_CHECKED(VixDiskLib_GetMetadataKeys(diskHandle, buf, bufsize, pointer(bufsize)))
	return filter(None, str(buf[:], 'utf-8').split('\0'))

def PyVixDiskLib_Open(connection, path, flags = VIXDISKLIB_FLAG_OPEN_READ_ONLY):
	retval = PyVixDiskLibHandle()
	_VIXDISKLIB_CHECKED(VixDiskLib_Open(connection, path, flags, pointer(retval)))
	return retval

def PyVixDiskLib_Read(diskHandle, startSector, numSectors):
	buf = ctypes.create_string_buffer(VIXDISKLIB_SECTOR_SIZE * numSectors)
	_VIXDISKLIB_CHECKED(VixDiskLib_Read(diskHandle, startSector, numSectors, buf))
	return buf[:]

def PyVixDiskLib_ReadMetadata(diskHandle, key):
	bufsize = c_size_t()
	VixDiskLib_ReadMetadata(diskHandle, key, c_char_p(0), 0, pointer(bufsize))
	buf = ctypes.create_string_buffer(bufsize.value)
	_VIXDISKLIB_CHECKED(VixDiskLib_ReadMetadata(diskHandle, key, buf, bufsize, pointer(bufsize)))
	return str(buf[:-1], 'utf-8')

def PyVixDiskLib_Shrink(diskHandle, progressFunc = None, *params):
	@VixDiskLibProgressFunc
	def thunk(progressCallbackData, progress):
		return bool(progressFunc(progress, *params))
	_VIXDISKLIB_CHECKED(VixDiskLib_Shrink(diskHandle, _PyDefaultVixDiskLibProgressFunc if progressFunc is None else thunk, NULL))

def PyVixDiskLib_SpaceNeededForClone(diskHandle, cloneDiskType = VixDiskLibDiskType.VIXDISKLIB_DISK_MONOLITHIC_FLAT):
	retval = c_uint64()
	_VIXDISKLIB_CHECKED(VixDiskLib_SpaceNeededForClone(diskHandle, cloneDiskType, pointer(retval)))
	return retval.value

def PyVixDiskLib_Write(diskHandle, startSector, numSectors, content):
	_VIXDISKLIB_CHECKED(VixDiskLib_Write(diskHandle, startSector, numSectors, content))

def _default_callback(progress, *args):
	print(progress, *args)
	return True

class PyVMDK:
	def __init__(self, trait):
		self.trait = trait

	def __del__(self):
		del self.trait

	def CreateChild(self, childPath, diskType = VixDiskLibDiskType.VIXDISKLIB_DISK_MONOLITHIC_SPARSE, progressFunc = _default_callback, *params):
		PyVixDiskLib_CreateChild(self.trait, childPath, diskType, progressFunc, *params)

	def Defragment(self, progressFunc = _default_callback, *params):
		PyVixDiskLib_Defragment(self.trait, progressFunc, *params)

	def GetInfo(self):
		return PyVixDiskLib_GetInfo(self.trait)

	def GetMetadataKeys(self):
		return PyVixDiskLib_GetMetadataKeys(self.trait)

	def Read(self, startSector, numSectors):
		return PyVixDiskLib_Read(self.trait, startSector, numSectors)

	def ReadMetadata(self, key):
		return PyVixDiskLib_ReadMetadata(self.trait, key)

	def Shrink(self, progressFunc = _default_callback, *params):
		PyVixDiskLib_Shrink(self.trait, progressFunc, *params)

	def SpaceNeededForClone(self, cloneDiskType = VixDiskLibDiskType.VIXDISKLIB_DISK_MONOLITHIC_FLAT):
		return PyVixDiskLib_SpaceNeededForClone(self.trait, cloneDiskType)

	def Write(self, startSector, numSectors, content):
		PyVixDiskLib_Write(self.trait, startSector, numSectors, content)

class PyVDDK:
	import atexit
	VixDiskLib_Init(VIXDISKLIB_VERSION_MAJOR, VIXDISKLIB_VERSION_MINOR, NULL, NULL, NULL, NULL)
	atexit.register(VixDiskLib_Exit)

	def __init__(self, *args):
		self.srcConnection = PyVixDiskLib_Connect(*args)

	def __del__(self):
		del self.srcConnection

	def Create(self, path, createParams, progressFunc = _default_callback, *params):
		PyVixDiskLib_Create(self.srcConnection, path, createParams, progressFunc, *params)

	def Open(self, path, flags = VIXDISKLIB_FLAG_OPEN_READ_ONLY):
		return PyVMDK(PyVixDiskLib_Open(self.srcConnection, path, flags))
