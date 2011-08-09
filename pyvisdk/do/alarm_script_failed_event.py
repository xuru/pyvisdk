
from pyvisdk.do.alarm_event import AlarmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmScriptFailedEvent(AlarmEvent):
    '''This event records a failure to complete an alarm-triggered script.
    '''
    
    def __init__(self, entity, reason, script):
        # MUST define these
        super(AlarmScriptFailedEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['reason'] = reason
        self.data['script'] = script
    
    
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
    def script(self):
        '''The script triggered by the alarm.
        '''
        return self.data['script']

