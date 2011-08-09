
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDpmHostConfigInfo(DynamicData):
    '''DPM configuration for a single host. This makes it possible to override the
        default behavior for an individual host.
    '''
    
    def __init__(self, behavior, enabled, key):
        # MUST define these
        super(ClusterDpmHostConfigInfo, self).__init__()
    
        self.data['behavior'] = behavior
        self.data['enabled'] = enabled
        self.data['key'] = key
    
    
    @property
    def behavior(self):
        '''Specifies the particular DPM behavior for this host.
        '''
        return self.data['behavior']

    @property
    def enabled(self):
        '''Flag to indicate whether or not VirtualCenter is allowed to perform any power
        related operations or recommendations for this host. If this flag is
        false, the host is effectively excluded from DPM service.
        '''
        return self.data['enabled']

    @property
    def key(self):
        '''Reference to the host.
        '''
        return self.data['key']

