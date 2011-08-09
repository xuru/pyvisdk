
from pyvisdk.do.scheduled_task_spec import ScheduledTaskSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskInfo(ScheduledTaskSpec):
    '''The scheduled task details.
    '''
    
    def __init__(self, activeTask, entity, error, lastModifiedTime, lastModifiedUser, nextRunTime, prevRunTime, progress, result, scheduledTask, state, taskObject):
        # MUST define these
        super(ScheduledTaskInfo, self).__init__()
    
        self.data['activeTask'] = activeTask
        self.data['entity'] = entity
        self.data['error'] = error
        self.data['lastModifiedTime'] = lastModifiedTime
        self.data['lastModifiedUser'] = lastModifiedUser
        self.data['nextRunTime'] = nextRunTime
        self.data['prevRunTime'] = prevRunTime
        self.data['progress'] = progress
        self.data['result'] = result
        self.data['scheduledTask'] = scheduledTask
        self.data['state'] = state
        self.data['taskObject'] = taskObject
    
    
    @property
    def activeTask(self):
        '''The running task instance when the scheduled task state is "running".
        '''
        return self.data['activeTask']

    @property
    def entity(self):
        '''The entity on which related events will be logged. If the task is scheduled on a
        ManagedEntity, this field will also reflect the same ManagedEntity. If
        task is scheduled on a ManagedObject, this field will have information
        about the entity on which the events will be logged on behalf of the
        ManagedObject. ManagedObject itself will be denoted by taskObject
        '''
        return self.data['entity']

    @property
    def error(self):
        '''The fault code when the scheduled task state is "error".
        '''
        return self.data['error']

    @property
    def lastModifiedTime(self):
        '''The time the scheduled task is created or modified.
        '''
        return self.data['lastModifiedTime']

    @property
    def lastModifiedUser(self):
        '''Last user that modified the scheduled task.
        '''
        return self.data['lastModifiedUser']

    @property
    def nextRunTime(self):
        '''The next time the scheduled task will run.
        '''
        return self.data['nextRunTime']

    @property
    def prevRunTime(self):
        '''The last time the scheduled task ran.
        '''
        return self.data['prevRunTime']

    @property
    def progress(self):
        '''The task progress when the scheduled task state is "running".
        '''
        return self.data['progress']

    @property
    def result(self):
        '''The operation result when the scheduled task state is "success".
        '''
        return self.data['result']

    @property
    def scheduledTask(self):
        '''Scheduled task object.
        '''
        return self.data['scheduledTask']

    @property
    def state(self):
        '''Scheduled task state.
        '''
        return self.data['state']

    @property
    def taskObject(self):
        '''The object on which the scheduled task is defined. This field will have
        information about either the ManagedEntity or the ManagedObject on which
        the scheduled task is defined.
        '''
        return self.data['taskObject']

