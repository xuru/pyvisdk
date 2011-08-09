
from pyvisdk.do.vm_relocate_spec_event import VmRelocateSpecEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmRelocateFailedEvent(VmRelocateSpecEvent):
    '''This event records a failure to relocate a virtual machine.
    '''
    
    def __init__(self, destHost, reason):
        # MUST define these
        super(VmRelocateFailedEvent, self).__init__()
    
        self.data['destHost'] = destHost
        self.data['reason'] = reason
    
    
    @property
    def destHost(self):
        '''The destination host to which the virtual machine is being relocated.
        '''
        return self.data['destHost']

    @property
    def reason(self):
        '''The reason why this relocate operation failed.
        '''
        return self.data['reason']

