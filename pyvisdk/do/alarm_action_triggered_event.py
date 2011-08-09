
from pyvisdk.do.alarm_event import AlarmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmActionTriggeredEvent(AlarmEvent):
    '''This event records that an alarm was triggered.
    '''
    
    def __init__(self, entity, source):
        # MUST define these
        super(AlarmActionTriggeredEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['source'] = source
    
    
    @property
    def entity(self):
        '''The entity with which the alarm is registered.
        '''
        return self.data['entity']

    @property
    def source(self):
        '''The entity that triggered the alarm.
        '''
        return self.data['source']

