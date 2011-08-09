
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineIdeDiskDevicePartitionInfo(DynamicData):
    '''Describes the partition sizes
    '''
    
    def __init__(self, capacity, id):
        # MUST define these
        super(VirtualMachineIdeDiskDevicePartitionInfo, self).__init__()
    
        self.data['capacity'] = capacity
        self.data['id'] = id
    
    
    @property
    def capacity(self):
        '''Size of partition
        '''
        return self.data['capacity']

    @property
    def id(self):
        '''Identification of the partition
        '''
        return self.data['id']

