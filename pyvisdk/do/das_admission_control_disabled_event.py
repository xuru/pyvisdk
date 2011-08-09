
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DasAdmissionControlDisabledEvent(ClusterEvent):
    '''This event records when admission control checks have been disabled in a HA
        cluster.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(DasAdmissionControlDisabledEvent, self).__init__()
    

    
    
