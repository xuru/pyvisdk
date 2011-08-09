
from pyvisdk.do.recurrent_task_scheduler import RecurrentTaskScheduler
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HourlyTaskScheduler(RecurrentTaskScheduler):
    '''The HourlyTaskScheduler data object sets the time for hourly task execution. By
        default, the scheduled task will run once every hour, at the specified
        minute.If you set the interval to a value greater than 1, the task will
        execute at the specified hourly interval. (For example, an interval of 2
        will cause the task to execute at the specified minute every 2 hours.)
    '''
    
    def __init__(self, minute):
        # MUST define these
        super(HourlyTaskScheduler, self).__init__()
    
        self.data['minute'] = minute
    
    
    @property
    def minute(self):
        '''The minute at which the RecurrentTaskScheduler runs the task. Specify the minute
        value as a UTC (Coordinated Univeral Time) value in the range 0 to 59.
        '''
        return self.data['minute']

