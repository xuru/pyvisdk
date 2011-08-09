
from pyvisdk.do.hourly_task_scheduler import HourlyTaskScheduler
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DailyTaskScheduler(HourlyTaskScheduler):
    '''The DailyTaskScheduler data object sets the time for daily task execution. You set
        the hour and the inherited minute property to complete the schedule. By
        default, the scheduled task will run once every day at the specified hour
        and minute.If you set the interval to a value greater than 1, the task
        will execute at the specified daily interval. (For example, an interval of
        2 will cause the task to execute at the specified hour and minute every 2
        days.)
    '''
    
    def __init__(self, hour):
        # MUST define these
        super(DailyTaskScheduler, self).__init__()
    
        self.data['hour'] = hour
    
    
    @property
    def hour(self):
        '''The hour at which the RecurrentTaskScheduler runs the task. Use UTC (Coordinated
        Universal Time) values in the range 0 to 23, where 0 = 12:00 a.m. (UTC)
        and 12 = 12:00 p.m. (UTC).
        '''
        return self.data['hour']

