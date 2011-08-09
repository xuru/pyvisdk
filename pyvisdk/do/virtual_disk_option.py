
from pyvisdk.do.virtual_device_option import VirtualDeviceOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskOption(VirtualDeviceOption):
    '''The VirtualDiskOption data class contains the options for the virtual disk data
        object type.
    '''
    
    def __init__(self, capacityInKB, ioAllocationOption):
        # MUST define these
        super(VirtualDiskOption, self).__init__()
    
        self.data['capacityInKB'] = capacityInKB
        self.data['ioAllocationOption'] = ioAllocationOption
    
    
    @property
    def capacityInKB(self):
        '''Minimum, maximum, and default capacity of the disk.
        '''
        return self.data['capacityInKB']

    @property
    def ioAllocationOption(self):
        '''Minumum, maximum, and default values for Storage I/O allocation.
        '''
        return self.data['ioAllocationOption']

