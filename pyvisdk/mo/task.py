
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Task(ExtensibleManagedObject):
    '''A task is used to monitor and potentially cancel long running operations.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Task):
        # MUST define these
        super(Task, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def info(self):
        '''Detailed information about this task.
        '''
        return self.update('info')


    def CancelTask(self, percentDone):
        '''Cancels a running or queued task. A task may only be canceled if it is cancelable.
        Multiple cancel requests will be treated as a single cancelation request.
        Canceling a completed or already canceled task will throw an InvalidState
        exception.If a task is canceled, its runtime state will be set to error
        and its error state will be set to RequestCanceled.A cancel operation is
        asynchronous. The operation may return before the task is canceled.

        :param percentDone: Percentage to set for this task

        '''
        
        return self.delegate("CancelTask")(percentDone)
        

    def SetTaskDescription(self, percentDone):
        '''Updates task description to describe the current phase of the task.

        :param percentDone: Percentage to set for this task

        '''
        
        return self.delegate("SetTaskDescription")(percentDone)
        

    def SetTaskState(self, percentDone):
        '''Sets task state and optionally sets results or fault, as appropriate for state

        :param percentDone: Percentage to set for this task

        '''
        
        return self.delegate("SetTaskState")(percentDone)
        

    def UpdateProgress(self, percentDone):
        '''Sets percentage done for this task and recalculates overall percentage done. If a
        percentDone value of less than zero or greater than 100 is specified, a
        value of zero or 100 respectively is used.

        :param percentDone: Percentage to set for this task

        '''
        
        return self.delegate("UpdateProgress")(percentDone)
        
