
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class InsufficientFailoverResourcesEvent(ClusterEvent):
    '''This event records that the cluster resources are insufficient to satisfy the
        configured HA failover level.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(InsufficientFailoverResourcesEvent, self).__init__()
    

    
    
