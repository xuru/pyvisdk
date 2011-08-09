
from pyvisdk.do.session_event import SessionEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserLoginSessionEvent(SessionEvent):
    '''This event records a user logon.
    '''
    
    def __init__(self, ipAddress, locale, sessionId):
        # MUST define these
        super(UserLoginSessionEvent, self).__init__()
    
        self.data['ipAddress'] = ipAddress
        self.data['locale'] = locale
        self.data['sessionId'] = sessionId
    
    
    @property
    def ipAddress(self):
        '''The IP address of the peer that initiated the connection. This may be the client
        that originated the session, or it may be an intervening proxy if the
        binding uses a protocol that supports proxies, such as HTTP.
        '''
        return self.data['ipAddress']

    @property
    def locale(self):
        '''The locale of the session.
        '''
        return self.data['locale']

    @property
    def sessionId(self):
        '''The unique identifier for the session.
        '''
        return self.data['sessionId']

