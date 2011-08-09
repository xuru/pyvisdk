
from pyvisdk.do.virtual_machine_target_info import VirtualMachineTargetInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineUsbInfo(VirtualMachineTargetInfo):
    '''This data object contains information about a physical USB device on the host.
    '''
    
    def __init__(self, description, family, physicalPath, product, speed, summary, vendor):
        # MUST define these
        super(VirtualMachineUsbInfo, self).__init__()
    
        self.data['description'] = description
        self.data['family'] = family
        self.data['physicalPath'] = physicalPath
        self.data['product'] = product
        self.data['speed'] = speed
        self.data['summary'] = summary
        self.data['vendor'] = vendor
    
    
    @property
    def description(self):
        '''A user visible name of the USB device.
        '''
        return self.data['description']

    @property
    def family(self):
        '''The device class families. For possible values see VirtualMachineUsbInfoFamily
        '''
        return self.data['family']

    @property
    def physicalPath(self):
        '''An autoconnect pattern which describes the device's physical path. This is the
        path to the specific port on the host where the USB device is attached.
        '''
        return self.data['physicalPath']

    @property
    def product(self):
        '''The product ID of the USB device.
        '''
        return self.data['product']

    @property
    def speed(self):
        '''The possible device speeds detected by server. For possible values see
        VirtualMachineUsbInfoSpeed
        '''
        return self.data['speed']

    @property
    def summary(self):
        '''Summary information about the virtual machine that is currently using this device,
        if any.
        '''
        return self.data['summary']

    @property
    def vendor(self):
        '''The vendor ID of the USB device.
        '''
        return self.data['vendor']

