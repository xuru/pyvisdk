
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NotEnoughResourcesToStartVmEvent(VmEvent):
    '''This event records when the HA does not find sufficient resources to failover a
        virtual machine.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(NotEnoughResourcesToStartVmEvent, self).__init__()
    

    
    
