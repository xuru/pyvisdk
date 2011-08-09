
from pyvisdk.do.task_scheduler import TaskScheduler
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AfterStartupTaskScheduler(TaskScheduler):
    '''The AfterStartupTaskScheduler data object establishes the time that a scheduled
        task will run after the vCenter server restarts.
    '''
    
    def __init__(self, minute):
        # MUST define these
        super(AfterStartupTaskScheduler, self).__init__()
    
        self.data['minute'] = minute
    
    
    @property
    def minute(self):
        '''The delay in minutes after vCenter server is restarted. The value must be greater
        than or equal to 0.
        '''
        return self.data['minute']

