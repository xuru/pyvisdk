
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFaultToleranceStateChangedEvent(VmEvent):
    '''This event records a fault tolerance state change. A default alarm will be
        triggered upon this event, which would change the vm state: the vm state
        is red if the newState is needSecondary; the vm state is yellow if the
        newState is disabled; the vm state is green if the newState is
        notConfigured, starting, enabled or running
    '''
    
    def __init__(self, newState, oldState):
        # MUST define these
        super(VmFaultToleranceStateChangedEvent, self).__init__()
    
        self.data['newState'] = newState
        self.data['oldState'] = oldState
    
    
    @property
    def newState(self):
        '''The new fault tolerance state.
        '''
        return self.data['newState']

    @property
    def oldState(self):
        '''The old fault toleeance state.
        '''
        return self.data['oldState']

