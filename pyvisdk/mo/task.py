
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Task(ExtensibleManagedObject):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Task):
        # MUST define these
        super(Task, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def info(self):
        '''Detailed information about this task.
        '''
        return self.update('info')


    def CancelTask(self):
        '''Cancels a running or queued task. A task may only be canceled if it is cancelable.
        Multiple cancel requests will be treated as a single cancelation request.
        Canceling a completed or already canceled task will throw an InvalidState
        exception.If a task is canceled, its runtime state will be set to error
        and its error state will be set to RequestCanceled.A cancel operation is
        asynchronous. The operation may return before the task is canceled.
        '''
        
        return self.delegate("CancelTask")()
        

    def SetTaskDescription(self, description):
        '''Updates task description to describe the current phase of the task.

        :param description: New description for task

        '''
        
        return self.delegate("SetTaskDescription")(description)
        

    def SetTaskState(self, state, result, fault):
        '''Sets task state and optionally sets results or fault, as appropriate for state

        :param state: New state for task

        :param result: Result to set, valid only if task state is TaskInfo.State.success

        :param fault: Fault to set, valid only if task state is error. The fault must be a of a fault
        type that directly or indirectly extends VimFault.

        '''
        
        return self.delegate("SetTaskState")(state,result,fault)
        

    def UpdateProgress(self, percentDone):
        '''Sets percentage done for this task and recalculates overall percentage done. If a
        percentDone value of less than zero or greater than 100 is specified, a
        value of zero or 100 respectively is used.

        :param percentDone: Percentage to set for this task

        '''
        
        return self.delegate("UpdateProgress")(percentDone)
        
