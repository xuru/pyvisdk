
from pyvisdk.do.session_event import SessionEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SessionTerminatedEvent(SessionEvent):
    '''This event records the termination of a session.
    '''
    
    def __init__(self, sessionId, terminatedUsername):
        # MUST define these
        super(SessionTerminatedEvent, self).__init__()
    
        self.data['sessionId'] = sessionId
        self.data['terminatedUsername'] = terminatedUsername
    
    
    @property
    def sessionId(self):
        '''The unique identifier of the terminated session.
        '''
        return self.data['sessionId']

    @property
    def terminatedUsername(self):
        '''The name of the user owning the terminated session.
        '''
        return self.data['terminatedUsername']

