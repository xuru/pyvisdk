
from pyvisdk.do.daily_task_scheduler import DailyTaskScheduler
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class WeeklyTaskScheduler(DailyTaskScheduler):
    '''The WeeklyTaskScheduler data object sets the time for weekly task execution. You
        can set the schedule for task execution on one or more days during the
        week, and you complete the schedule by setting the inherited properties
        for the hour and minute.By default the scheduler executes the task
        according to the specified day(s) every week. If you set the interval to a
        value greater than 1, the task will execute at the specified weekly
        interval. (For example, an interval of 2 will cause the task to execute on
        the specified days every 2 weeks.)
    '''
    
    def __init__(self, friday, monday, saturday, sunday, thursday, tuesday, wednesday):
        # MUST define these
        super(WeeklyTaskScheduler, self).__init__()
    
        self.data['friday'] = friday
        self.data['monday'] = monday
        self.data['saturday'] = saturday
        self.data['sunday'] = sunday
        self.data['thursday'] = thursday
        self.data['tuesday'] = tuesday
        self.data['wednesday'] = wednesday
    
    
    @property
    def friday(self):
        '''
        '''
        return self.data['friday']

    @property
    def monday(self):
        '''
        '''
        return self.data['monday']

    @property
    def saturday(self):
        '''
        '''
        return self.data['saturday']

    @property
    def sunday(self):
        '''The day or days of the week when the scheduled task will run. At least one of the
        days must be true.
        '''
        return self.data['sunday']

    @property
    def thursday(self):
        '''
        '''
        return self.data['thursday']

    @property
    def tuesday(self):
        '''
        '''
        return self.data['tuesday']

    @property
    def wednesday(self):
        '''
        '''
        return self.data['wednesday']

