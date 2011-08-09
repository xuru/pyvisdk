
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNasVolumeSpec(DynamicData):
    '''Specification for creating NAS volume.
    '''
    
    def __init__(self, accessMode, localPath, password, remoteHost, remotePath, type, userName):
        # MUST define these
        super(HostNasVolumeSpec, self).__init__()
    
        self.data['accessMode'] = accessMode
        self.data['localPath'] = localPath
        self.data['password'] = password
        self.data['remoteHost'] = remoteHost
        self.data['remotePath'] = remotePath
        self.data['type'] = type
        self.data['userName'] = userName
    
    
    @property
    def accessMode(self):
        '''Access mode for the mount point.
        '''
        return self.data['accessMode']

    @property
    def localPath(self):
        '''The localPath refers to the name of the NAS datastore to be created using this
        specification.
        '''
        return self.data['localPath']

    @property
    def password(self):
        '''If type is CIFS, the password to use when connecting to the CIFS server. If type
        is NFS, this field will be ignored.
        '''
        return self.data['password']

    @property
    def remoteHost(self):
        '''The host that runs the NFS server.
        '''
        return self.data['remoteHost']

    @property
    def remotePath(self):
        '''The remote path of the NFS mount point.
        '''
        return self.data['remotePath']

    @property
    def type(self):
        '''The type of the the NAS volume (CIFS / NFS). If not specified, defaults to nfs.
        '''
        return self.data['type']

    @property
    def userName(self):
        '''If type is CIFS, the user name to use when connecting to the CIFS server. If type
        is NFS, this field will be ignored.
        '''
        return self.data['userName']

