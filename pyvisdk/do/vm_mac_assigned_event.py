
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmMacAssignedEvent(VmEvent):
    '''This event records the assignment of a new MAC address to a virtual network
        adapter.
    '''
    
    def __init__(self, adapter, mac):
        # MUST define these
        super(VmMacAssignedEvent, self).__init__()
    
        self.data['adapter'] = adapter
        self.data['mac'] = mac
    
    
    @property
    def adapter(self):
        '''The name of the virtual adapter.
        '''
        return self.data['adapter']

    @property
    def mac(self):
        '''The new MAC address.
        '''
        return self.data['mac']

