
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmNoCompatibleHostForSecondaryEvent(VmEvent):
    '''This event records that no compatible host was found to place a secondary VM. A
        default alarm will be triggered upon this event, which by default would
        trigger a SNMP trap.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VmNoCompatibleHostForSecondaryEvent, self).__init__()
    

    
    
