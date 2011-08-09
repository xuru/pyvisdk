
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmRelayoutUpToDateEvent(VmEvent):
    '''This event records that a virtual machine is already in the correct format. No
        relay out is necessary.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VmRelayoutUpToDateEvent, self).__init__()
    

    
    
