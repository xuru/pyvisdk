
from pyvisdk.do.virtual_device_option import VirtualDeviceOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualUSBOption(VirtualDeviceOption):
    '''The VirtualUSBOption data object type contains options for USB device
        configuration on a virtual machine. The vSphere API supports the following
        options:* Local host USB connection (VirtualUSBUSBBackingOption) * Remote
        host USB connection (VirtualUSBRemoteHostBackingOption)For information
        about USB device configuration, see VirtualUSB.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VirtualUSBOption, self).__init__()
    

    
    
