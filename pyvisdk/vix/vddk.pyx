# cython: profile=True

from common cimport malloc, free, uint16, uint32, uint64, va_list, strdup, Bool

cdef extern from "vixDiskLib.h":
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
        
    ctypedef struct VixDiskLibTicketIdCreds
    union VixDiskLibCreds:
        VixDiskLibUidPasswdCreds uid
        VixDiskLibSessionIdCreds sessionId
        VixDiskLibTicketIdCreds *ticketId

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
        
    ctypedef struct VixDiskLibHandleStruct
    ctypedef VixDiskLibHandleStruct *VixDiskLibHandle

    ctypedef struct VixDiskLibConnectParam
    ctypedef VixDiskLibConnectParam *VixDiskLibConnection

    # callbacks 
    ctypedef void (*VixDiskLibGenericLogFunc)(char *fmt, va_list args)
    ctypedef Bool (*VixDiskLibProgressFunc)(void *progressData, int percentCompleted)

    # initialize the library
    VixError VixDiskLib_InitEx(uint32 majorVersion, uint32 minorVersion, VixDiskLibGenericLogFunc *log,
                  VixDiskLibGenericLogFunc *warn, VixDiskLibGenericLogFunc *panic, char* libDir,
                  char* configFile)
    VixError VixDiskLib_Init(uint32 majorVersion, uint32 minorVersion, VixDiskLibGenericLogFunc *log,
                VixDiskLibGenericLogFunc *warn, VixDiskLibGenericLogFunc *panic, char* libDir)
    void VixDiskLib_Exit()
    
    # connect
    VixError VixDiskLib_ConnectEx(VixDiskLibConnectParams *connectParams,
             Bool readOnly, char *snapshotRef, char *transportModes, VixDiskLibConnection *connection)
    VixError VixDiskLib_Connect(VixDiskLibConnectParams *connectParams, VixDiskLibConnection *connection)
    void VixDiskLib_FreeConnectParams(VixDiskLibConnectParams* connectParams)

    # get info
    VixError VixDiskLib_GetInfo(VixDiskLibHandle diskHandle, VixDiskLibInfo **info)
    void VixDiskLib_FreeInfo(VixDiskLibInfo *info)
    
    # error text
    char * VixDiskLib_GetErrorText(VixError err, char *locale)
    void VixDiskLib_FreeErrorText(char* errMsg)



cdef class VDDK(object):
    cdef char *hostname
    cdef VixDiskLibConnectParams connectParams
    cdef VixDiskLibConnection srcConnection
    
    def __init__(self, hostname):
        self.hostname = strdup(hostname)
        
    def __dealloc__(self):
        if self.hostname != NULL:
            free(self.hostname)

    def connect(self, char *username, char *password):
        print "Connecting to %s as %s" % (self.hostname, username)
    
        self.connectParams.serverName = self.hostname
        self.connectParams.creds.uid.userName = username
        self.connectParams.creds.uid.password = password
        self.connectParams.port = 902
    
        vixError = VixDiskLib_Init(1, 0, NULL, NULL, NULL, NULL)
        vixError = VixDiskLib_Connect(&(self.connectParams), &(self.srcConnection))
    
    def close(self):
        VixDiskLib_FreeConnectParams(&self.connectParams)
        VixDiskLib_Exit()
    
# ----------------------------------------------------------------------
# vim: set filetype=python expandtab shiftwidth=4:
# [X]Emacs local variables declaration - place us into python mode
# Local Variables:
# mode:python
# py-indent-offset:4
# End: