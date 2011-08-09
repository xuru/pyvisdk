
from pyvisdk.do.vm_powered_off_event import VmPoweredOffEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmPowerOffOnIsolationEvent(VmPoweredOffEvent):
    '''This event records when a virtual machine has been powered off on an isolated host
        in a HA cluster.
    '''
    
    def __init__(self, isolatedHost):
        # MUST define these
        super(VmPowerOffOnIsolationEvent, self).__init__()
    
        self.data['isolatedHost'] = isolatedHost
    
    
    @property
    def isolatedHost(self):
        '''The isolated host on which a virtual machine is powered off.
        '''
        return self.data['isolatedHost']

