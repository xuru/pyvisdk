
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmPoweringOnWithCustomizedDVPortEvent(VmEvent):
    '''This event records when a virtual machine was powering on using DVPorts with port
        level configuration, which might be different from the DVportgroup.
    '''
    
    def __init__(self, vnic):
        # MUST define these
        super(VmPoweringOnWithCustomizedDVPortEvent, self).__init__()
    
        self.data['vnic'] = vnic
    
    
    @property
    def vnic(self):
        '''The list of vnic that were using the DVports.
        '''
        return self.data['vnic']

