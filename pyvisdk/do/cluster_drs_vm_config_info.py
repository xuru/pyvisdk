
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDrsVmConfigInfo(DynamicData):
    '''DRS configuration for a single virtual machine. This makes it possible to override
        the default behavior for an individual virtual machine.
    '''
    
    def __init__(self, behavior, enabled, key):
        # MUST define these
        super(ClusterDrsVmConfigInfo, self).__init__()
    
        self.data['behavior'] = behavior
        self.data['enabled'] = enabled
        self.data['key'] = key
    
    
    @property
    def behavior(self):
        '''Specifies the particular DRS behavior for this virtual machine.
        '''
        return self.data['behavior']

    @property
    def enabled(self):
        '''Flag to indicate whether or not VirtualCenter is allowed to perform any DRS
        migration or initial placement recommendations for this virtual machine.
        If this flag is false, the virtual machine is effectively excluded from
        DRS.
        '''
        return self.data['enabled']

    @property
    def key(self):
        '''Reference to the virtual machine.
        '''
        return self.data['key']

