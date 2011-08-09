
from pyvisdk.do.virtual_device_option import VirtualDeviceOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualControllerOption(VirtualDeviceOption):
    '''The VirtualControllerOption data object type contains information about a virtual
        controller type.
    '''
    
    def __init__(self, devices, supportedDevice):
        # MUST define these
        super(VirtualControllerOption, self).__init__()
    
        self.data['devices'] = devices
        self.data['supportedDevice'] = supportedDevice
    
    
    @property
    def devices(self):
        '''The minimum and maximum number of devices this controller can control at run time.
        '''
        return self.data['devices']

    @property
    def supportedDevice(self):
        '''Array of supported device options for this controller.
        '''
        return self.data['supportedDevice']

