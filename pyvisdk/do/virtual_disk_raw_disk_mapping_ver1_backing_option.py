
from pyvisdk.do.virtual_device_device_backing_option import VirtualDeviceDeviceBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskRawDiskMappingVer1BackingOption(VirtualDeviceDeviceBackingOption):
    '''The VirtualDiskOption.RawDiskMappingVer1BackingOption object type contains the
        available options when backing a virtual disk using a raw device mapping
        on ESX Server 2.5 or 3.x.
    '''
    
    def __init__(self, compatibilityMode, descriptorFileNameExtensions, diskMode, uuid):
        # MUST define these
        super(VirtualDiskRawDiskMappingVer1BackingOption, self).__init__()
    
        self.data['compatibilityMode'] = compatibilityMode
        self.data['descriptorFileNameExtensions'] = descriptorFileNameExtensions
        self.data['diskMode'] = diskMode
        self.data['uuid'] = uuid
    
    
    @property
    def compatibilityMode(self):
        '''The supported raw disk mapping compatibility modes.
        '''
        return self.data['compatibilityMode']

    @property
    def descriptorFileNameExtensions(self):
        '''Valid extensions for the filename of the optional raw disk mapping descriptor
        file. This is present only for ESX Server 3.x and greater hosts.
        '''
        return self.data['descriptorFileNameExtensions']

    @property
    def diskMode(self):
        '''The disk mode. Valid values are: * persistent * independent_persistent *
        independent_nonpersistent
        '''
        return self.data['diskMode']

    @property
    def uuid(self):
        '''Flag to indicate whether this backing supports disk UUID property.
        '''
        return self.data['uuid']

