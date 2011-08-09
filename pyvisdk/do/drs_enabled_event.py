
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DrsEnabledEvent(ClusterEvent):
    '''This event records when DRS is enabled on a cluster.
    '''
    
    def __init__(self, behavior):
        # MUST define these
        super(DrsEnabledEvent, self).__init__()
    
        self.data['behavior'] = behavior
    
    
    @property
    def behavior(self):
        '''The DRS automation level in (DrsBehavior)
        '''
        return self.data['behavior']

