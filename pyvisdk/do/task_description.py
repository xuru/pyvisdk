
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskDescription(DynamicData):
    '''Static strings for task objects. These strings are locale-specific.
    '''
    
    def __init__(self, methodInfo, reason, state):
        # MUST define these
        super(TaskDescription, self).__init__()
    
        self.data['methodInfo'] = methodInfo
        self.data['reason'] = reason
        self.data['state'] = state
    
    
    @property
    def methodInfo(self):
        '''Display label and summary for all tasks
        '''
        return self.data['methodInfo']

    @property
    def reason(self):
        '''Kind of entity responsible for creating this task.
        '''
        return self.data['reason']

    @property
    def state(self):
        '''TaskInfo State enum
        '''
        return self.data['state']

