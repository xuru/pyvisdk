
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFailedMigrateEvent(VmEvent):
    '''This event records a failure to migrate a virtual machine.
    '''
    
    def __init__(self, destHost, reason):
        # MUST define these
        super(VmFailedMigrateEvent, self).__init__()
    
        self.data['destHost'] = destHost
        self.data['reason'] = reason
    
    
    @property
    def destHost(self):
        '''The destination host.
        '''
        return self.data['destHost']

    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

