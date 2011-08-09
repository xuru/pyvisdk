
from pyvisdk.do.task_event import TaskEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskTimeoutEvent(TaskEvent):
    '''This event records when a task is cleaned up b/c of timeout
    '''
    
    def __init__(self, ):
        # MUST define these
        super(TaskTimeoutEvent, self).__init__()
    

    
    
