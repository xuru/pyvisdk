
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmReconfiguredEvent(VmEvent):
    '''This event records a reconfiguration of the virtual machine.
    '''
    
    def __init__(self, configSpec):
        # MUST define these
        super(VmReconfiguredEvent, self).__init__()
    
        self.data['configSpec'] = configSpec
    
    
    @property
    def configSpec(self):
        '''The configuration specification that was used for the reconfiguration.
        '''
        return self.data['configSpec']

