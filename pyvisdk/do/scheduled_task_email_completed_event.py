
from pyvisdk.do.scheduled_task_event import ScheduledTaskEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskEmailCompletedEvent(ScheduledTaskEvent):
    '''This event records the sending of a notification via email for a scheduled task.
    '''
    
    def __init__(self, to):
        # MUST define these
        super(ScheduledTaskEmailCompletedEvent, self).__init__()
    
        self.data['to'] = to
    
    
    @property
    def to(self):
        '''The destination email address.
        '''
        return self.data['to']

