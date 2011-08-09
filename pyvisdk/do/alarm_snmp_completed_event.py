
from pyvisdk.do.alarm_event import AlarmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmSnmpCompletedEvent(AlarmEvent):
    '''This event records the completion of an alarm SNMP notification.
    '''
    
    def __init__(self, entity):
        # MUST define these
        super(AlarmSnmpCompletedEvent, self).__init__()
    
        self.data['entity'] = entity
    
    
    @property
    def entity(self):
        '''The entity with which the alarm is registered.
        '''
        return self.data['entity']

