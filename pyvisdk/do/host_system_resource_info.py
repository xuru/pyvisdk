
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSystemResourceInfo(DynamicData):
    '''The SystemResourceInfo data object describes the configuration of a single system
        resource group. System resource groups are analogous to ResourcePool
        objects for virtual machines; however, their structure is fixed and groups
        may not be created nor destroyed, only configured.
    '''
    
    def __init__(self, child, config, key):
        # MUST define these
        super(HostSystemResourceInfo, self).__init__()
    
        self.data['child'] = child
        self.data['config'] = config
        self.data['key'] = key
    
    
    @property
    def child(self):
        '''List of child resource groups.
        '''
        return self.data['child']

    @property
    def config(self):
        '''Configuration of this system resource group.
        '''
        return self.data['config']

    @property
    def key(self):
        '''ID of the system resource group.
        '''
        return self.data['key']

