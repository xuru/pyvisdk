
from pyvisdk.do.alarm_spec import AlarmSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmInfo(AlarmSpec):
    '''Attributes of an alarm.
    '''
    
    def __init__(self, alarm, creationEventId, entity, key, lastModifiedTime, lastModifiedUser):
        # MUST define these
        super(AlarmInfo, self).__init__()
    
        self.data['alarm'] = alarm
        self.data['creationEventId'] = creationEventId
        self.data['entity'] = entity
        self.data['key'] = key
        self.data['lastModifiedTime'] = lastModifiedTime
        self.data['lastModifiedUser'] = lastModifiedUser
    
    
    @property
    def alarm(self):
        '''The alarm object.
        '''
        return self.data['alarm']

    @property
    def creationEventId(self):
        '''The event ID that records the alarm creation.
        '''
        return self.data['creationEventId']

    @property
    def entity(self):
        '''The entity on which the alarm is registered.
        '''
        return self.data['entity']

    @property
    def key(self):
        '''The unique key.
        '''
        return self.data['key']

    @property
    def lastModifiedTime(self):
        '''The time the alarm was created or modified.
        '''
        return self.data['lastModifiedTime']

    @property
    def lastModifiedUser(self):
        '''User name that modified the alarm most recently.
        '''
        return self.data['lastModifiedUser']

