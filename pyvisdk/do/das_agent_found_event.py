
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DasAgentFoundEvent(ClusterEvent):
    '''This event records that VirtualCenter has re-established contact with a primary
        host in this HA cluster.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(DasAgentFoundEvent, self).__init__()
    

    
    
