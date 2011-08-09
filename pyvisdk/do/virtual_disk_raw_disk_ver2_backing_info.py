
from pyvisdk.do.virtual_device_device_backing_info import VirtualDeviceDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskRawDiskVer2BackingInfo(VirtualDeviceDeviceBackingInfo):
    '''This data object type contains information about backing a virtual disk by using a
        host device, as used by VMware Server.
    '''
    
    def __init__(self, changeId, descriptorFileName, uuid):
        # MUST define these
        super(VirtualDiskRawDiskVer2BackingInfo, self).__init__()
    
        self.data['changeId'] = changeId
        self.data['descriptorFileName'] = descriptorFileName
        self.data['uuid'] = uuid
    
    
    @property
    def changeId(self):
        '''The change ID of the virtual disk for the corresponding snapshot or virtual
        machine. This can be used to track incremental changes to a virtual disk.
        See QueryChangedDiskAreas.
        '''
        return self.data['changeId']

    @property
    def descriptorFileName(self):
        '''The name of the raw disk descriptor file.
        '''
        return self.data['descriptorFileName']

    @property
    def uuid(self):
        '''Disk UUID for the virtual disk, if available.
        '''
        return self.data['uuid']

