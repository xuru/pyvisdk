
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmMigratedEvent(VmEvent):
    '''This event records a virtual machine migration.
    '''
    
    def __init__(self, sourceHost):
        # MUST define these
        super(VmMigratedEvent, self).__init__()
    
        self.data['sourceHost'] = sourceHost
    
    
    @property
    def sourceHost(self):
        '''The source host. (Because this is after a successful migration, the destination
        host is recorded in the inherited "host" property.)
        '''
        return self.data['sourceHost']

