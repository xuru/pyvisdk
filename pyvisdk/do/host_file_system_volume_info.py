
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFileSystemVolumeInfo(DynamicData):
    '''The HostFileSystemVolumeInfo data object describes the file system volume
        information for the host.A file system volume refers to a storage
        abstraction that allows files to be created and organized. A host can have
        multiple file system volumes. File system volumes are typically mounted
        into a file namespace that allows all files in mounted file systems to be
        addressable from the host.A file system volume is backed by disk storage.
        It could span one or more disks but need not use an entire disk.A file
        system volume by definition must be mounted on the file system in order to
        exist.
    '''
    
    def __init__(self, mountInfo, volumeTypeList):
        # MUST define these
        super(HostFileSystemVolumeInfo, self).__init__()
    
        self.data['mountInfo'] = mountInfo
        self.data['volumeTypeList'] = volumeTypeList
    
    
    @property
    def mountInfo(self):
        '''The list of file system volumes mounted on the host.
        '''
        return self.data['mountInfo']

    @property
    def volumeTypeList(self):
        '''The list of supported file system volume types.
        '''
        return self.data['volumeTypeList']

