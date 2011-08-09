
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmMacChangedEvent(VmEvent):
    '''This event records a change in a virtual machine's MAC address.
    '''
    
    def __init__(self, adapter, newMac, oldMac):
        # MUST define these
        super(VmMacChangedEvent, self).__init__()
    
        self.data['adapter'] = adapter
        self.data['newMac'] = newMac
        self.data['oldMac'] = oldMac
    
    
    @property
    def adapter(self):
        '''The name of the virtual network adapter.
        '''
        return self.data['adapter']

    @property
    def newMac(self):
        '''The new MAC address.
        '''
        return self.data['newMac']

    @property
    def oldMac(self):
        '''The old MAC address.
        '''
        return self.data['oldMac']

