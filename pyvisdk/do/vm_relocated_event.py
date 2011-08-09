
from pyvisdk.do.vm_relocate_spec_event import VmRelocateSpecEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmRelocatedEvent(VmRelocateSpecEvent):
    '''This event records the completion of a virtual machine relocation.
    '''
    
    def __init__(self, sourceHost):
        # MUST define these
        super(VmRelocatedEvent, self).__init__()
    
        self.data['sourceHost'] = sourceHost
    
    
    @property
    def sourceHost(self):
        '''The source host from which the virtual machine was relocated.
        '''
        return self.data['sourceHost']

