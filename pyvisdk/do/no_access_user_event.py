
from pyvisdk.do.session_event import SessionEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NoAccessUserEvent(SessionEvent):
    '''This event records a failed user logon due to insufficient access permission.
    '''
    
    def __init__(self, ipAddress):
        # MUST define these
        super(NoAccessUserEvent, self).__init__()
    
        self.data['ipAddress'] = ipAddress
    
    
    @property
    def ipAddress(self):
        '''The IP address of the peer that initiated the connection. This may be the client
        that originated the session, or it may be an intervening proxy if the
        binding uses a protocol that supports proxies, such as HTTP.
        '''
        return self.data['ipAddress']

