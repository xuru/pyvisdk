
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterOvercommittedEvent(ClusterEvent):
    '''This event records when a cluster's host capacity cannot satisfy resource
        configuration constraints.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(ClusterOvercommittedEvent, self).__init__()
    

    
    
