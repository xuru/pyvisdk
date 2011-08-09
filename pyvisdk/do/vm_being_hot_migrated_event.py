
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmBeingHotMigratedEvent(VmEvent):
    '''This event records that a virtual machine is being hot-migrated.
    '''
    
    def __init__(self, destHost):
        # MUST define these
        super(VmBeingHotMigratedEvent, self).__init__()
    
        self.data['destHost'] = destHost
    
    
    @property
    def destHost(self):
        '''The destination host to which the virtual machine is to be migrated.
        '''
        return self.data['destHost']

