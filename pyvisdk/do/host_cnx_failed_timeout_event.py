
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCnxFailedTimeoutEvent(HostEvent):
    '''This event records a failure to connect to a host due to a timeout on the
        connection attempt.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostCnxFailedTimeoutEvent, self).__init__()
    

    
    
