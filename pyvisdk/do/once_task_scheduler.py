
from pyvisdk.do.task_scheduler import TaskScheduler
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OnceTaskScheduler(TaskScheduler):
    '''The OnceTaskScheduler data object establishes the time for running a scheduled
        task only once.
    '''
    
    def __init__(self, runAt):
        # MUST define these
        super(OnceTaskScheduler, self).__init__()
    
        self.data['runAt'] = runAt
    
    
    @property
    def runAt(self):
        '''The time a task will run. If you do not set the time, it executes immediately.
        '''
        return self.data['runAt']

