
from pyvisdk.do.task_scheduler import TaskScheduler
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class RecurrentTaskScheduler(TaskScheduler):
    '''The RecurrentTaskScheduler data object is the base type for the hierarchy that
        includes hourly, daily, weekly, and monthly task schedulers.
    '''
    
    def __init__(self, interval):
        # MUST define these
        super(RecurrentTaskScheduler, self).__init__()
    
        self.data['interval'] = interval
    
    
    @property
    def interval(self):
        '''How often to run the scheduled task. The value must be greater than or equal to 1.
        The default value is 1. The interval acts as a multiplier for the unit of
        time associated with a particular scheduler (hours, days, weeks, or
        months). For example, setting the HourlyTaskScheduler interval to 4 causes
        the task to run every 4 hours.
        '''
        return self.data['interval']

