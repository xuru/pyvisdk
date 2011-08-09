
from pyvisdk.do.alarm_event import AlarmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmEmailFailedEvent(AlarmEvent):
    '''This event records a failure to complete an alarm email notification.
    '''
    
    def __init__(self, entity, reason, to):
        # MUST define these
        super(AlarmEmailFailedEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['reason'] = reason
        self.data['to'] = to
    
    
    @property
    def entity(self):
        '''The entity with which the alarm is registered.
        '''
        return self.data['entity']

    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

    @property
    def to(self):
        '''The destination email address.
        '''
        return self.data['to']

