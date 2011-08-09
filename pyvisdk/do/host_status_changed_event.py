
from pyvisdk.do.cluster_status_changed_event import ClusterStatusChangedEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostStatusChangedEvent(ClusterStatusChangedEvent):
    '''This event records when a host's overall status changed.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostStatusChangedEvent, self).__init__()
    

    
    
