# cython: profile=True

cdef extern from "vixDiskLib.h":
    ctypedef long long uint64
    ctypedef long uint32
    ctypedef int uint16

    ctypedef uint64 VixDiskLibSectorType
    ctypedef uint64 VixError

    enum VixDiskLibDiskType:
        VIXDISKLIB_DISK_MONOLITHIC_SPARSE         = 1,   # monolithic file, sparse
        VIXDISKLIB_DISK_MONOLITHIC_FLAT           = 2,   # monolithic file,
                                                         # all space pre-allocated
        VIXDISKLIB_DISK_SPLIT_SPARSE              = 3,   # disk split into 2GB extents,
                                                         # sparse
        VIXDISKLIB_DISK_SPLIT_FLAT                = 4,   # disk split into 2GB extents,
                                                         # pre-allocated
        VIXDISKLIB_DISK_VMFS_FLAT                 = 5,   # ESX 3.0 and above flat disks
        VIXDISKLIB_DISK_STREAM_OPTIMIZED          = 6,   # compressed monolithic sparse
        VIXDISKLIB_DISK_VMFS_THIN                 = 7,   # ESX 3.0 and above thin provisioned
        VIXDISKLIB_DISK_VMFS_SPARSE               = 8,   # ESX 3.0 and above sparse disks
        VIXDISKLIB_DISK_UNKNOWN                   = 256  # unknown type

    enum VixDiskLibAdapterType:
        VIXDISKLIB_ADAPTER_IDE                    = 1,
        VIXDISKLIB_ADAPTER_SCSI_BUSLOGIC          = 2,
        VIXDISKLIB_ADAPTER_SCSI_LSILOGIC          = 3,
        VIXDISKLIB_ADAPTER_UNKNOWN                = 256

    struct VixDiskLibCreateParams:
        VixDiskLibDiskType           diskType
        VixDiskLibAdapterType        adapterType
        uint16                       hwVersion
        VixDiskLibSectorType         capacity

    struct VixDiskLibUidPasswdCreds:
         char *userName # User id and password on the
         char *password # VC/ESX host.

    struct VixDiskLibSessionIdCreds:
        char *cookie
        char *userName
        char *key

    enum VixDiskLibCredType:
        VIXDISKLIB_CRED_UID                      = 1, # use userid password
        VIXDISKLIB_CRED_SESSIONID                = 2, # http session id
        VIXDISKLIB_CRED_TICKETID                 = 3, # vim ticket id
        VIXDISKLIB_CRED_SSPI                     = 4, # Windows only - use current thread credentials.
        VIXDISKLIB_CRED_UNKNOWN                  = 256

    union VixDiskLibCreds:
        VixDiskLibUidPasswdCreds uid
        VixDiskLibSessionIdCreds sessionId

    struct VixDiskLibConnectParams:
        char *vmxSpec     # URL like spec of the VM.
        char *serverName  # Name or IP address of VC / ESX.
        VixDiskLibCredType credType

        VixDiskLibCreds creds
        uint32 port

    struct VixDiskLibGeometry:
        uint32 cylinders
        uint32 heads
        uint32 sectors

    struct VixDiskLibInfo:
        VixDiskLibGeometry   biosGeo      # BIOS geometry for booting and partitioning
        VixDiskLibGeometry   physGeo      # physical geometry
        VixDiskLibSectorType capacity     # total capacity in sectors
        VixDiskLibAdapterType adapterType # adapter type
        int numLinks                      # number of links (i.e. base disk + redo logs)
        char *parentFileNameHint          # parent file for a redo log

    VixError VixDiskLib_InitEx(uint32 majorVersion, uint32 minorVersion, VixDiskLibGenericLogFunc *log,
                  VixDiskLibGenericLogFunc *warn, VixDiskLibGenericLogFunc *panic, char* libDir,
                  char* configFile)
    VixError VixDiskLib_Init(uint32 majorVersion, uint32 minorVersion, VixDiskLibGenericLogFunc *log,
                VixDiskLibGenericLogFunc *warn, VixDiskLibGenericLogFunc *panic, char* libDir)

def connect(char *server, char *username, char *password):
    print "Connecting to %s as %s" % (server, username)

    VixDiskLibConnectParams connectParams
    VixDiskLibConnection srcConnection

    connectParams.serverName = server
    connectParams.creds.uid.userName = username
    connectParams.creds.uid.password = password
    connectParams.port = 902;

    vixError = VixDiskLib_Init(1, 0, NULL, NULL, NULL, NULL);
    vixError = VixDiskLib_Connect(&connectParams, &srcConnection);