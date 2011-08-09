
from pyvisdk.do.alarm_event import AlarmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmReconfiguredEvent(AlarmEvent):
    '''This event records the reconfiguration of an alarm.
    '''
    
    def __init__(self, entity):
        # MUST define these
        super(AlarmReconfiguredEvent, self).__init__()
    
        self.data['entity'] = entity
    
    
    @property
    def entity(self):
        '''The entity with which the alarm is registered.
        '''
        return self.data['entity']

