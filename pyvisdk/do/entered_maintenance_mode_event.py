
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EnteredMaintenanceModeEvent(HostEvent):
    '''This event records that the host has completely entered maintenance mode. A host
        in this mode has no running virtual machines and no provisioning
        operations are occuring.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(EnteredMaintenanceModeEvent, self).__init__()
    

    
    
