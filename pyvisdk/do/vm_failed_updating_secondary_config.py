
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFailedUpdatingSecondaryConfig(VmEvent):
    '''This event records after a failover the new new primary failed to update the
        config of the secondary vm.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VmFailedUpdatingSecondaryConfig, self).__init__()
    

    
    
