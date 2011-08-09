
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmInstanceUuidAssignedEvent(VmEvent):
    '''This event records the assignment of a new instance UUID to a virtual machine.
    '''
    
    def __init__(self, instanceUuid):
        # MUST define these
        super(VmInstanceUuidAssignedEvent, self).__init__()
    
        self.data['instanceUuid'] = instanceUuid
    
    
    @property
    def instanceUuid(self):
        '''The new instance UUID.
        '''
        return self.data['instanceUuid']

