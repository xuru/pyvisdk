
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmHealthMonitoringStateChangedEvent(ClusterEvent):
    '''This event records when host monitoring state has changed.
    '''
    
    def __init__(self, state):
        # MUST define these
        super(VmHealthMonitoringStateChangedEvent, self).__init__()
    
        self.data['state'] = state
    
    
    @property
    def state(self):
        '''The service state in ClusterDasConfigInfoVmMonitoringState
        '''
        return self.data['state']

