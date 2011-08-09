
from pyvisdk.do.vm_powered_off_event import VmPoweredOffEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmShutdownOnIsolationEvent(VmPoweredOffEvent):
    '''This event records when a virtual machine has been shut down on an isolated host
        in a HA cluster.
    '''
    
    def __init__(self, isolatedHost, shutdownResult):
        # MUST define these
        super(VmShutdownOnIsolationEvent, self).__init__()
    
        self.data['isolatedHost'] = isolatedHost
        self.data['shutdownResult'] = shutdownResult
    
    
    @property
    def isolatedHost(self):
        '''The isolated host on which a virtual machine was shutdown.
        '''
        return self.data['isolatedHost']

    @property
    def shutdownResult(self):
        '''Indicates if the shutdown was successful. If the shutdown failed, the virtual
        machine was powered off. see Operation
        '''
        return self.data['shutdownResult']

