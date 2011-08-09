
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmInstanceUuidChangedEvent(VmEvent):
    '''This event records a change in a virtual machine's instance UUID.
    '''
    
    def __init__(self, newInstanceUuid, oldInstanceUuid):
        # MUST define these
        super(VmInstanceUuidChangedEvent, self).__init__()
    
        self.data['newInstanceUuid'] = newInstanceUuid
        self.data['oldInstanceUuid'] = oldInstanceUuid
    
    
    @property
    def newInstanceUuid(self):
        '''The new instance UUID.
        '''
        return self.data['newInstanceUuid']

    @property
    def oldInstanceUuid(self):
        '''The old instance UUID.
        '''
        return self.data['oldInstanceUuid']

