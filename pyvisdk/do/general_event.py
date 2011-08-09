
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GeneralEvent(Event):
    '''These are general events.
    '''
    
    def __init__(self, message):
        # MUST define these
        super(GeneralEvent, self).__init__()
    
        self.data['message'] = message
    
    
    @property
    def message(self):
        '''A short form of the message string, not localized.
        '''
        return self.data['message']

