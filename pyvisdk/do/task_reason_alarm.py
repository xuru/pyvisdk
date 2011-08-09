
from pyvisdk.do.task_reason import TaskReason
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskReasonAlarm(TaskReason):
    '''Indicates that the task was queued by an alarm.
    '''
    
    def __init__(self, alarm, alarmName, entity, entityName):
        # MUST define these
        super(TaskReasonAlarm, self).__init__()
    
        self.data['alarm'] = alarm
        self.data['alarmName'] = alarmName
        self.data['entity'] = entity
        self.data['entityName'] = entityName
    
    
    @property
    def alarm(self):
        '''The alarm object that queued the task.
        '''
        return self.data['alarm']

    @property
    def alarmName(self):
        '''The name of the alarm that queued the task, retained in the history collector
        database.
        '''
        return self.data['alarmName']

    @property
    def entity(self):
        '''The managed entity object on which the alarm is triggered.
        '''
        return self.data['entity']

    @property
    def entityName(self):
        '''The name of the managed entity on which the alarm is triggered, retained in the
        history collector database.
        '''
        return self.data['entityName']

