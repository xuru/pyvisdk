
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskEvent(Event):
    '''This event records the creation of a Task. Note that the embedded TaskInfo object
        is a of the Task state at the time of its creation, so its state will
        always be "queued". To find the current status of the task, query for the
        current state of the Task using the eventChainId in the embedded TaskInfo
        object.
    '''
    
    def __init__(self, info):
        # MUST define these
        super(TaskEvent, self).__init__()
    
        self.data['info'] = info
    
    
    @property
    def info(self):
        '''The information about the task.
        '''
        return self.data['info']

