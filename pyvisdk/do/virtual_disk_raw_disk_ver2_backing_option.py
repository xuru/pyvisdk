
from pyvisdk.do.virtual_device_device_backing_option import VirtualDeviceDeviceBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskRawDiskVer2BackingOption(VirtualDeviceDeviceBackingOption):
    '''The VirtualDiskOption.RawDiskVer2BackingOption object type contains the available
        options when backing a virtual disk using a host device on VMware Server.
    '''
    
    def __init__(self, descriptorFileNameExtensions, uuid):
        # MUST define these
        super(VirtualDiskRawDiskVer2BackingOption, self).__init__()
    
        self.data['descriptorFileNameExtensions'] = descriptorFileNameExtensions
        self.data['uuid'] = uuid
    
    
    @property
    def descriptorFileNameExtensions(self):
        '''Valid extensions for the filename of the raw disk descriptor file.
        '''
        return self.data['descriptorFileNameExtensions']

    @property
    def uuid(self):
        '''Flag to indicate whether this backing supports disk UUID property.
        '''
        return self.data['uuid']

