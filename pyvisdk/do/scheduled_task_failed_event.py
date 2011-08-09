
from pyvisdk.do.scheduled_task_event import ScheduledTaskEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskFailedEvent(ScheduledTaskEvent):
    '''This event records the failure of a scheduled task.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(ScheduledTaskFailedEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

