
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostHardwareStatusInfo(DynamicData):
    '''Data object representing the status of the hardware components of the host.
    '''
    
    def __init__(self, cpuStatusInfo, memoryStatusInfo, storageStatusInfo):
        # MUST define these
        super(HostHardwareStatusInfo, self).__init__()
    
        self.data['cpuStatusInfo'] = cpuStatusInfo
        self.data['memoryStatusInfo'] = memoryStatusInfo
        self.data['storageStatusInfo'] = storageStatusInfo
    
    
    @property
    def cpuStatusInfo(self):
        '''Status of the CPU packages
        '''
        return self.data['cpuStatusInfo']

    @property
    def memoryStatusInfo(self):
        '''Status of the physical memory
        '''
        return self.data['memoryStatusInfo']

    @property
    def storageStatusInfo(self):
        '''Status of the physical storage system
        '''
        return self.data['storageStatusInfo']

