
from pyvisdk.do.task_reason import TaskReason
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskReasonUser(TaskReason):
    '''Indicates that the task was queued by a specific user.
    '''
    
    def __init__(self, userName):
        # MUST define these
        super(TaskReasonUser, self).__init__()
    
        self.data['userName'] = userName
    
    
    @property
    def userName(self):
        '''Name of the user that queued the task.
        '''
        return self.data['userName']

