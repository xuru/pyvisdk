
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourceConfigOption(DynamicData):
    '''This data object type is a default value and value range specification for
        ResourceConfigSpec object.
    '''
    
    def __init__(self, cpuAllocationOption, memoryAllocationOption):
        # MUST define these
        super(ResourceConfigOption, self).__init__()
    
        self.data['cpuAllocationOption'] = cpuAllocationOption
        self.data['memoryAllocationOption'] = memoryAllocationOption
    
    
    @property
    def cpuAllocationOption(self):
        '''Resource allocation options for CPU.
        '''
        return self.data['cpuAllocationOption']

    @property
    def memoryAllocationOption(self):
        '''Resource allocation options for memory.
        '''
        return self.data['memoryAllocationOption']

