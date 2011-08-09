
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFaultToleranceTurnedOffEvent(VmEvent):
    '''This event records that all secondary virtual machines have been removed and fault
        tolerance protection turned off for this virtual machine.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VmFaultToleranceTurnedOffEvent, self).__init__()
    

    
    
