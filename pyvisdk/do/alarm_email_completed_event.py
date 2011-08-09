
from pyvisdk.do.alarm_event import AlarmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmEmailCompletedEvent(AlarmEvent):
    '''This event records the completion of an alarm email notification.
    '''
    
    def __init__(self, entity, to):
        # MUST define these
        super(AlarmEmailCompletedEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['to'] = to
    
    
    @property
    def entity(self):
        '''The entity with which the alarm is registered.
        '''
        return self.data['entity']

    @property
    def to(self):
        '''The destination email address.
        '''
        return self.data['to']

