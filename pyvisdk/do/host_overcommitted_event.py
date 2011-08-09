
from pyvisdk.do.cluster_overcommitted_event import ClusterOvercommittedEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostOvercommittedEvent(ClusterOvercommittedEvent):
    '''This event records when a host's capacity cannot satisfy resource configuration
        constraints.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostOvercommittedEvent, self).__init__()
    

    
    
