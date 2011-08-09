
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskMappingPartitionOption(DynamicData):
    '''The PhysicalPartitionOption data class contains the options for a partition on a
        physical disk.
    '''
    
    def __init__(self, capacityInKb, fileSystem, name):
        # MUST define these
        super(HostDiskMappingPartitionOption, self).__init__()
    
        self.data['capacityInKb'] = capacityInKb
        self.data['fileSystem'] = fileSystem
        self.data['name'] = name
    
    
    @property
    def capacityInKb(self):
        '''Partition capacity, in KB.
        '''
        return self.data['capacityInKb']

    @property
    def fileSystem(self):
        '''File system, if the partition is formatted.
        '''
        return self.data['fileSystem']

    @property
    def name(self):
        '''Partition name.
        '''
        return self.data['name']

