
from pyvisdk.do.vm_powered_on_event import VmPoweredOnEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmRestartedOnAlternateHostEvent(VmPoweredOnEvent):
    '''This event records that the virtual machine was restarted on a host, since its
        original host had failed.
    '''
    
    def __init__(self, sourceHost):
        # MUST define these
        super(VmRestartedOnAlternateHostEvent, self).__init__()
    
        self.data['sourceHost'] = sourceHost
    
    
    @property
    def sourceHost(self):
        '''The host that failed.
        '''
        return self.data['sourceHost']

