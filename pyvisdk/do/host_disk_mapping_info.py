
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskMappingInfo(DynamicData):
    '''The HostDiskMappingInfo data object type describes a virtual disk mapping to a
        host disk.
    '''
    
    def __init__(self, exclusive, name, physicalPartition):
        # MUST define these
        super(HostDiskMappingInfo, self).__init__()
    
        self.data['exclusive'] = exclusive
        self.data['name'] = name
        self.data['physicalPartition'] = physicalPartition
    
    
    @property
    def exclusive(self):
        '''Flag to indicate whether or not the virtual machine has exclusive access to the
        host device.
        '''
        return self.data['exclusive']

    @property
    def name(self):
        '''Host resource name.
        '''
        return self.data['name']

    @property
    def physicalPartition(self):
        '''The partition used on the host, if not mapping to a full disk device.
        '''
        return self.data['physicalPartition']

