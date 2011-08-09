
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostGetShortNameFailedEvent(HostEvent):
    '''This event records that hostname -s failed or returned a name containing '.'.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostGetShortNameFailedEvent, self).__init__()
    

    
    
