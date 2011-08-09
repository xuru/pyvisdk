
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmState(DynamicData):
    '''Information about the alarm's state.
    '''
    
    def __init__(self, acknowledged, acknowledgedByUser, acknowledgedTime, alarm, entity, key, overallStatus, time):
        # MUST define these
        super(AlarmState, self).__init__()
    
        self.data['acknowledged'] = acknowledged
        self.data['acknowledgedByUser'] = acknowledgedByUser
        self.data['acknowledgedTime'] = acknowledgedTime
        self.data['alarm'] = alarm
        self.data['entity'] = entity
        self.data['key'] = key
        self.data['overallStatus'] = overallStatus
        self.data['time'] = time
    
    
    @property
    def acknowledged(self):
        '''Flag to indicate if the alarm's actions have been acknowledged for the associated
        ManagedEntity.
        '''
        return self.data['acknowledged']

    @property
    def acknowledgedByUser(self):
        '''The user who acknowledged this triggering. If the triggering has not been
        acknowledged, then the value is not valid.
        '''
        return self.data['acknowledgedByUser']

    @property
    def acknowledgedTime(self):
        '''The time this triggering was acknowledged. If the triggering has not been
        acknowledged, then the value is not valid.
        '''
        return self.data['acknowledgedTime']

    @property
    def alarm(self):
        '''Alarm object from which the AlarmState object is instantiated.
        '''
        return self.data['alarm']

    @property
    def entity(self):
        '''Entity on which the alarm is instantiated.
        '''
        return self.data['entity']

    @property
    def key(self):
        '''Unique key that identifies the alarm.
        '''
        return self.data['key']

    @property
    def overallStatus(self):
        '''Overall status of the alarm object. This is the value of the alarm's top-level
        expression.
        '''
        return self.data['overallStatus']

    @property
    def time(self):
        '''Time the alarm triggered.
        '''
        return self.data['time']

