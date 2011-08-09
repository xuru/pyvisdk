
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots(DynamicData):
    '''
    '''
    
    def __init__(self, host, slots):
        # MUST define these
        super(ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots, self).__init__()
    
        self.data['host'] = host
        self.data['slots'] = slots
    
    
    @property
    def host(self):
        '''The reference to the host.
        '''
        return self.data['host']

    @property
    def slots(self):
        '''The number of slots in this host.
        '''
        return self.data['slots']

