
from pyvisdk.do.monthly_task_scheduler import MonthlyTaskScheduler
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MonthlyByWeekdayTaskScheduler(MonthlyTaskScheduler):
    '''The MonthlyByWeekdayTaskScheduler data object sets the time for monthly task
        execution. You identify a single day for task execution by specifying the
        week of the month and day of the week, and you complete the schedule by
        setting the inherited properties for the hour and minute.By default, the
        scheduler executes the task on the specified day every month. If you set
        the interval to a value greater than 1, the task will execute at the
        specified monthly interval. (For example, an interval of 2 will cause the
        task to execute on the specified day, hour, and minute every 2 months.)
    '''
    
    def __init__(self, offset, weekday):
        # MUST define these
        super(MonthlyByWeekdayTaskScheduler, self).__init__()
    
        self.data['offset'] = offset
        self.data['weekday'] = weekday
    
    
    @property
    def offset(self):
        '''The week in the month during which the scheduled task is to run.
        '''
        return self.data['offset']

    @property
    def weekday(self):
        '''The day in the week when the scheduled task is to run.
        '''
        return self.data['weekday']

