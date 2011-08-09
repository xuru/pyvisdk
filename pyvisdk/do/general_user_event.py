
from pyvisdk.do.general_event import GeneralEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GeneralUserEvent(GeneralEvent):
    '''This event is the general user event type.
    '''
    
    def __init__(self, entity):
        # MUST define these
        super(GeneralUserEvent, self).__init__()
    
        self.data['entity'] = entity
    
    
    @property
    def entity(self):
        '''The entity on which the event was logged.
        '''
        return self.data['entity']

