
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePoolSummary(DynamicData):
    '''This data object type encapsulates a typical set of resource pool information that
        is useful for list views and summary pages.
    '''
    
    def __init__(self, config, configuredMemoryMB, name, quickStats, runtime):
        # MUST define these
        super(ResourcePoolSummary, self).__init__()
    
        self.data['config'] = config
        self.data['configuredMemoryMB'] = configuredMemoryMB
        self.data['name'] = name
        self.data['quickStats'] = quickStats
        self.data['runtime'] = runtime
    
    
    @property
    def config(self):
        '''Current configuration of the resource pool.
        '''
        return self.data['config']

    @property
    def configuredMemoryMB(self):
        '''Total configured memory of all virtual machines in the resource pool, in MB.
        '''
        return self.data['configuredMemoryMB']

    @property
    def name(self):
        '''Name of resource pool.
        '''
        return self.data['name']

    @property
    def quickStats(self):
        '''A set of statistics that are typically updated with near real-time regularity.
        This data object type does not support notification, for scalability
        reasons. Therefore, changes in QuickStats do not generate property
        collector updates. To monitor statistics values, use the statistics and
        alarms modules instead.
        '''
        return self.data['quickStats']

    @property
    def runtime(self):
        '''Current runtime state of the resource pool.
        '''
        return self.data['runtime']

