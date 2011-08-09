
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmNoNetworkAccessEvent(VmEvent):
    '''This event records a migration failure when the destination host is not on the
        same network as the source host.
    '''
    
    def __init__(self, destHost):
        # MUST define these
        super(VmNoNetworkAccessEvent, self).__init__()
    
        self.data['destHost'] = destHost
    
    
    @property
    def destHost(self):
        '''The destination host.
        '''
        return self.data['destHost']

