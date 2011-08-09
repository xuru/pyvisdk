
from pyvisdk.do.session_event import SessionEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlreadyAuthenticatedSessionEvent(SessionEvent):
    '''This event records a failed user logon due to the user already being logged on.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(AlreadyAuthenticatedSessionEvent, self).__init__()
    

    
    
