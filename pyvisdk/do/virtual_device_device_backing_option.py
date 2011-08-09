
from pyvisdk.do.virtual_device_backing_option import VirtualDeviceBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceDeviceBackingOption(VirtualDeviceBackingOption):
    '''The DeviceBackingOption data class contains device-specific backing options.
    '''
    
    def __init__(self, autoDetectAvailable):
        # MUST define these
        super(VirtualDeviceDeviceBackingOption, self).__init__()
    
        self.data['autoDetectAvailable'] = autoDetectAvailable
    
    
    @property
    def autoDetectAvailable(self):
        '''Flag to indicate whether the specific instance of this device can be auto-detected
        on the host instead of having to specify a particular physical device.
        '''
        return self.data['autoDetectAvailable']

