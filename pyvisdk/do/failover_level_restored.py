
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FailoverLevelRestored(ClusterEvent):
    '''This event records that the amount of cluster resources has increased and is now
        sufficient to satisfy the configured HA failover level.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(FailoverLevelRestored, self).__init__()
    

    
    
