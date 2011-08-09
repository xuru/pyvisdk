
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmUuidChangedEvent(VmEvent):
    '''This event records a change in a virtual machine's BIOS UUID.
    '''
    
    def __init__(self, newUuid, oldUuid):
        # MUST define these
        super(VmUuidChangedEvent, self).__init__()
    
        self.data['newUuid'] = newUuid
        self.data['oldUuid'] = oldUuid
    
    
    @property
    def newUuid(self):
        '''The new BIOS UUID.
        '''
        return self.data['newUuid']

    @property
    def oldUuid(self):
        '''The old BIOS UUID.
        '''
        return self.data['oldUuid']

