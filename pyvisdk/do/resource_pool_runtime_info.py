
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePoolRuntimeInfo(DynamicData):
    '''Current runtime resource usage and state of the resource pool
    '''
    
    def __init__(self, cpu, memory, overallStatus):
        # MUST define these
        super(ResourcePoolRuntimeInfo, self).__init__()
    
        self.data['cpu'] = cpu
        self.data['memory'] = memory
        self.data['overallStatus'] = overallStatus
    
    
    @property
    def cpu(self):
        '''Runtime resource usage for CPU. Values are in Mhz.
        '''
        return self.data['cpu']

    @property
    def memory(self):
        '''Runtime resource usage for memory. Values are in bytes.
        '''
        return self.data['memory']

    @property
    def overallStatus(self):
        '''Overall health of the tree. See header for description of various statuses and
        when they are set
        '''
        return self.data['overallStatus']

