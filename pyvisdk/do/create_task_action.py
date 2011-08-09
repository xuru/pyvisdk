
from pyvisdk.do.action import Action
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CreateTaskAction(Action):
    '''This data object type specifies the type of task to be created when this action is
        triggered.
    '''
    
    def __init__(self, cancelable, taskTypeId):
        # MUST define these
        super(CreateTaskAction, self).__init__()
    
        self.data['cancelable'] = cancelable
        self.data['taskTypeId'] = taskTypeId
    
    
    @property
    def cancelable(self):
        '''Whether the task should be cancelable.
        '''
        return self.data['cancelable']

    @property
    def taskTypeId(self):
        '''Extension registered task type identifier for type of task being created.
        '''
        return self.data['taskTypeId']

