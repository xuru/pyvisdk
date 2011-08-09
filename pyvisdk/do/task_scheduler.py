
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskScheduler(DynamicData):
    '''The TaskScheduler data object is the base type for the scheduler objects. The
        hierarchy of scheduler objects is as follows:Use a scheduler object to set
        the time(s) for task execution. You can use two scheduling modes - single
        execution or recurring execution:* Use the AfterStartupTaskScheduler or
        the OnceTaskScheduler to schedule a single instance of task execution. *
        Use one of the recurrent task schedulers to schedule hourly, daily,
        weekly, or monthly task execution.After you have established the task
        timing, use the scheduler object for the ScheduledTaskSpec scheduler
        property value.
    '''
    
    def __init__(self, activeTime, expireTime):
        # MUST define these
        super(TaskScheduler, self).__init__()
    
        self.data['activeTime'] = activeTime
        self.data['expireTime'] = expireTime
    
    
    @property
    def activeTime(self):
        '''The time that the schedule for the task takes effect. Task activation is distinct
        from task execution. When you activate a task, its schedule starts, and
        when the next execution time occurs, the task will run. If you do not set
        activeTime, the activation time defaults to the time that you create the
        scheduled task.
        '''
        return self.data['activeTime']

    @property
    def expireTime(self):
        '''The time the schedule for the task expires. If you do not set expireTime, the
        schedule does not expire.
        '''
        return self.data['expireTime']

