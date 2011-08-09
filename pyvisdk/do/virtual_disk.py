
from pyvisdk.do.virtual_device import VirtualDevice
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDisk(VirtualDevice):
    '''This data object type contains information about a disk in a virtual machine.The
        virtual disk backing object types describe the different virtual disk
        backings available. The disk format version in each case describes the
        version of the format that is used.Supported virtual disk backings:
    '''
    
    def __init__(self, capacityInKB, shares, storageIOAllocation):
        # MUST define these
        super(VirtualDisk, self).__init__()
    
        self.data['capacityInKB'] = capacityInKB
        self.data['shares'] = shares
        self.data['storageIOAllocation'] = storageIOAllocation
    
    
    @property
    def capacityInKB(self):
        '''Capacity of this virtual disk.
        '''
        return self.data['capacityInKB']

    @property
    def shares(self):
        '''Disk shares, used for resource scheduling.
        '''
        return self.data['shares']

    @property
    def storageIOAllocation(self):
        '''Resource allocation for storage I/O.
        '''
        return self.data['storageIOAllocation']

