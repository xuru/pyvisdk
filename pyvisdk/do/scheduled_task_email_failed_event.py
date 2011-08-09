
from pyvisdk.do.scheduled_task_event import ScheduledTaskEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskEmailFailedEvent(ScheduledTaskEvent):
    '''This event records the failure of an attempt to send a notification via email for
        a scheduled task.
    '''
    
    def __init__(self, reason, to):
        # MUST define these
        super(ScheduledTaskEmailFailedEvent, self).__init__()
    
        self.data['reason'] = reason
        self.data['to'] = to
    
    
    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

    @property
    def to(self):
        '''The destination email address.
        '''
        return self.data['to']

