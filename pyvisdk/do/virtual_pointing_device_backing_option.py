
from pyvisdk.do.virtual_device_device_backing_option import VirtualDeviceDeviceBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualPointingDeviceBackingOption(VirtualDeviceDeviceBackingOption):
    '''The DeviceBackingOption data object type represents the options for a pointing
        device backing a VirtualPointingDevice data object type.
    '''
    
    def __init__(self, hostPointingDevice):
        # MUST define these
        super(VirtualPointingDeviceBackingOption, self).__init__()
    
        self.data['hostPointingDevice'] = hostPointingDevice
    
    
    @property
    def hostPointingDevice(self):
        '''This object defines the supported mouse types, including the default supported
        mouse type, with the following properties: *
        '''
        return self.data['hostPointingDevice']

