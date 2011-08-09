
from pyvisdk.do.alarm_event import AlarmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmScriptCompleteEvent(AlarmEvent):
    '''This event records the completion of an alarm-triggered script.
    '''
    
    def __init__(self, entity, script):
        # MUST define these
        super(AlarmScriptCompleteEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['script'] = script
    
    
    @property
    def entity(self):
        '''The entity with which the alarm is registered.
        '''
        return self.data['entity']

    @property
    def script(self):
        '''The script triggered by the alarm.
        '''
        return self.data['script']

