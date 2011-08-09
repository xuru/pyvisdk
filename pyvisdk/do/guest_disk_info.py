
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestDiskInfo(DynamicData):
    '''Information about each virtual disk configured in the guest operating system.
    '''
    
    def __init__(self, capacity, diskPath, freeSpace):
        # MUST define these
        super(GuestDiskInfo, self).__init__()
    
        self.data['capacity'] = capacity
        self.data['diskPath'] = diskPath
        self.data['freeSpace'] = freeSpace
    
    
    @property
    def capacity(self):
        '''Total capacity of the disk, in bytes. This is part of the virtual machine
        configuration.
        '''
        return self.data['capacity']

    @property
    def diskPath(self):
        '''Name of the virtual disk in the guest operating system. For example: C:\
        '''
        return self.data['diskPath']

    @property
    def freeSpace(self):
        '''Free space on the disk, in bytes. This is retrieved by VMware Tools.
        '''
        return self.data['freeSpace']

