
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskMappingOption(DynamicData):
    '''The HostDiskMappingOption data object type describes the options for a virtual
        disk mapping to a host disk.
    '''
    
    def __init__(self, name, physicalPartition):
        # MUST define these
        super(HostDiskMappingOption, self).__init__()
    
        self.data['name'] = name
        self.data['physicalPartition'] = physicalPartition
    
    
    @property
    def name(self):
        '''Host resource name.
        '''
        return self.data['name']

    @property
    def physicalPartition(self):
        '''Array of valid partitions on this physical disk. There is no default for this
        array.
        '''
        return self.data['physicalPartition']

