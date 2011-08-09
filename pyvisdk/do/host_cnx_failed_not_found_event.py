
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCnxFailedNotFoundEvent(HostEvent):
    '''This event records a failure to connect to a host due to a failure to resolve the
        host name.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostCnxFailedNotFoundEvent, self).__init__()
    

    
    
