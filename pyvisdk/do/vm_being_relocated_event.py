
from pyvisdk.do.vm_relocate_spec_event import VmRelocateSpecEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmBeingRelocatedEvent(VmRelocateSpecEvent):
    '''This event records that a virtual machine is being relocated.
    '''
    
    def __init__(self, destHost):
        # MUST define these
        super(VmBeingRelocatedEvent, self).__init__()
    
        self.data['destHost'] = destHost
    
    
    @property
    def destHost(self):
        '''The destination host to which the virtual machine is being relocated.
        '''
        return self.data['destHost']

