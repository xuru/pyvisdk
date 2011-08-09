
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmBeingMigratedEvent(VmEvent):
    '''This event records that a virtual machine is being migrated.
    '''
    
    def __init__(self, destHost):
        # MUST define these
        super(VmBeingMigratedEvent, self).__init__()
    
        self.data['destHost'] = destHost
    
    
    @property
    def destHost(self):
        '''The destination host.
        '''
        return self.data['destHost']

