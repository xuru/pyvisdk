
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCnxFailedBadUsernameEvent(HostEvent):
    '''This event records a failure to connect to a host due to an invalid user name and
        password combination.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostCnxFailedBadUsernameEvent, self).__init__()
    

    
    
