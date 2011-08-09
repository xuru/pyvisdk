
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostLocalFileSystemVolumeSpec(DynamicData):
    '''The specification for creating a new local file system volume.
    '''
    
    def __init__(self, device, localPath):
        # MUST define these
        super(HostLocalFileSystemVolumeSpec, self).__init__()
    
        self.data['device'] = device
        self.data['localPath'] = localPath
    
    
    @property
    def device(self):
        '''The device of the local file system.
        '''
        return self.data['device']

    @property
    def localPath(self):
        '''The file path on the host where the file system is mounted.
        '''
        return self.data['localPath']

