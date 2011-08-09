
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFileSystemMountInfo(DynamicData):
    '''The HostFileSystemMountInfo data object describes a host mount point for a file
        system.
    '''
    
    def __init__(self, mountInfo, volume, vStorageSupport):
        # MUST define these
        super(HostFileSystemMountInfo, self).__init__()
    
        self.data['mountInfo'] = mountInfo
        self.data['volume'] = volume
        self.data['vStorageSupport'] = vStorageSupport
    
    
    @property
    def mountInfo(self):
        '''Information about the mount point.
        '''
        return self.data['mountInfo']

    @property
    def volume(self):
        '''Information about the mounted volume.
        '''
        return self.data['volume']

    @property
    def vStorageSupport(self):
        '''vStorage hardware acceleration support status. This property represents the
        volume's capability for storage acceleration. See
        FileSystemMountInfoVStorageSupportStatus for valid values.
        '''
        return self.data['vStorageSupport']

