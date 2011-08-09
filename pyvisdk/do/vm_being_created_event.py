
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmBeingCreatedEvent(VmEvent):
    '''This event records a virtual machine being created.
    '''
    
    def __init__(self, configSpec):
        # MUST define these
        super(VmBeingCreatedEvent, self).__init__()
    
        self.data['configSpec'] = configSpec
    
    
    @property
    def configSpec(self):
        '''The configuration specification that was used to create this virtual machine.
        '''
        return self.data['configSpec']

