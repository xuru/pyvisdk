
from pyvisdk.do.host_file_system_volume import HostFileSystemVolume
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNasVolume(HostFileSystemVolume):
    '''This data object type describes the NAS volume. Applies to both NFS and CIFS.
    '''
    
    def __init__(self, remoteHost, remotePath, userName):
        # MUST define these
        super(HostNasVolume, self).__init__()
    
        self.data['remoteHost'] = remoteHost
        self.data['remotePath'] = remotePath
        self.data['userName'] = userName
    
    
    @property
    def remoteHost(self):
        '''The host that runs the NFS/CIFS server.
        '''
        return self.data['remoteHost']

    @property
    def remotePath(self):
        '''The remote path of NFS/CIFS mount point.
        '''
        return self.data['remotePath']

    @property
    def userName(self):
        '''In case of CIFS, the user name used while connecting to the server.
        '''
        return self.data['userName']

