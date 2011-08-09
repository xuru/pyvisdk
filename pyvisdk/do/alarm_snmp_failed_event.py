
from pyvisdk.do.alarm_event import AlarmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmSnmpFailedEvent(AlarmEvent):
    '''This event records a failure to complete an alarm SNMP notification.
    '''
    
    def __init__(self, entity, reason):
        # MUST define these
        super(AlarmSnmpFailedEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['reason'] = reason
    
    
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

