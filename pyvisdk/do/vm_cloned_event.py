
from pyvisdk.do.vm_clone_event import VmCloneEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmClonedEvent(VmCloneEvent):
    '''This event records the completion of a virtual machine cloning operation.
    '''
    
    def __init__(self, sourceVm):
        # MUST define these
        super(VmClonedEvent, self).__init__()
    
        self.data['sourceVm'] = sourceVm
    
    
    @property
    def sourceVm(self):
        '''The source virtual machine for the clone operation.
        '''
        return self.data['sourceVm']

