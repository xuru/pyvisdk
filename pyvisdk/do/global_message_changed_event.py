
from pyvisdk.do.session_event import SessionEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GlobalMessageChangedEvent(SessionEvent):
    '''This event records a change to the global message.
    '''
    
    def __init__(self, message):
        # MUST define these
        super(GlobalMessageChangedEvent, self).__init__()
    
        self.data['message'] = message
    
    
    @property
    def message(self):
        '''The new message that was set.
        '''
        return self.data['message']

