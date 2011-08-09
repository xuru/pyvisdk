
from pyvisdk.do.virtual_device_option import VirtualDeviceOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualSerialPortOption(VirtualDeviceOption):
    '''The data object contains the options for configuring the virtual serial port
        device defined by the data object. These options include information about
        how the device is backed physically on the host: by a network socket, a
        host file, a host serial port device, or a pipe to another process.
    '''
    
    def __init__(self, yieldOnPoll):
        # MUST define these
        super(VirtualSerialPortOption, self).__init__()
    
        self.data['yieldOnPoll'] = yieldOnPoll
    
    
    @property
    def yieldOnPoll(self):
        '''Indicates whether the virtual machine supports the CPU yield option during virtual
        serial port polling. When this feature is supported and enabled, the
        virtual machine will periodically relinquish the processor if its sole
        task is polling the virtual serial port.
        '''
        return self.data['yieldOnPoll']

