
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MigrationEvent(VmEvent):
    '''These are events used to describe migration warning and errors
    '''
    
    def __init__(self, fault):
        # MUST define these
        super(MigrationEvent, self).__init__()
    
        self.data['fault'] = fault
    
    
    @property
    def fault(self):
        '''The fault that describes the migration issue. This is typically either a
        MigrationFault or a VmConfigFault.
        '''
        return self.data['fault']

