
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmResourcePoolMovedEvent(VmEvent):
    '''This event records when a virtual machine is moved from one resource pool to
        another.
    '''
    
    def __init__(self, newParent, oldParent):
        # MUST define these
        super(VmResourcePoolMovedEvent, self).__init__()
    
        self.data['newParent'] = newParent
        self.data['oldParent'] = oldParent
    
    
    @property
    def newParent(self):
        '''The new parent resourcePool of the moved virtual machine.
        '''
        return self.data['newParent']

    @property
    def oldParent(self):
        '''The old parent resourcePool of the moved virtual machine.
        '''
        return self.data['oldParent']

