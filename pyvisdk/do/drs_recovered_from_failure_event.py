
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DrsRecoveredFromFailureEvent(ClusterEvent):
    '''This event records that DRS has recovered from failure. It is triggered by a
        successful DRS invocation after repeated failure.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(DrsRecoveredFromFailureEvent, self).__init__()
    

    
    
