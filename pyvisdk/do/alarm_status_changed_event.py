
from pyvisdk.do.alarm_event import AlarmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmStatusChangedEvent(AlarmEvent):
    '''This event records a status change for an alarm.
    '''
    
    def __init__(self, entity, from, source, to):
        # MUST define these
        super(AlarmStatusChangedEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['from'] = from
        self.data['source'] = source
        self.data['to'] = to
    
    
    @property
    def entity(self):
        '''The entity with which the alarm is registered.
        '''
        return self.data['entity']

    @property
    def from_(self):
        '''The original alarm status.
        '''
        return self.data['from']

    @property
    def source(self):
        '''The entity for which the alarm status has been changed.
        '''
        return self.data['source']

    @property
    def to(self):
        '''The new alarm status.
        '''
        return self.data['to']

