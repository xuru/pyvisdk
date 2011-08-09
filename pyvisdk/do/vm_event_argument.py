
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmEventArgument(EntityEventArgument):
    '''The event argument is a VirtualMachine object.
    '''
    
    def __init__(self, vm):
        # MUST define these
        super(VmEventArgument, self).__init__()
    
        self.data['vm'] = vm
    
    
    @property
    def vm(self):
        '''The VirtualMachine object.
        '''
        return self.data['vm']

