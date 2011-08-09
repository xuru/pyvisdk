
from pyvisdk.do.session_event import SessionEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class BadUsernameSessionEvent(SessionEvent):
    '''This event records a failed user logon. Failed logons are due to no match existing
        between the provided user name and password combination and the
        combinations stored for authentication.
    '''
    
    def __init__(self, ipAddress):
        # MUST define these
        super(BadUsernameSessionEvent, self).__init__()
    
        self.data['ipAddress'] = ipAddress
    
    
    @property
    def ipAddress(self):
        '''The IP address of the peer that initiated the connection. This may be the client
        that originated the session, or it may be an intervening proxy if the
        binding uses a protocol that supports proxies, such as HTTP.
        '''
        return self.data['ipAddress']

