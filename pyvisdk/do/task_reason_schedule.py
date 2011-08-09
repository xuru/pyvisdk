
from pyvisdk.do.task_reason import TaskReason
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskReasonSchedule(TaskReason):
    '''Indicates that the task was queued by a scheduled task.
    '''
    
    def __init__(self, name, scheduledTask):
        # MUST define these
        super(TaskReasonSchedule, self).__init__()
    
        self.data['name'] = name
        self.data['scheduledTask'] = scheduledTask
    
    
    @property
    def name(self):
        '''The name of the scheduled task that queued this task.
        '''
        return self.data['name']

    @property
    def scheduledTask(self):
        '''The scheduledTask object that queued this task.
        '''
        return self.data['scheduledTask']

