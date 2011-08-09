
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EnteredStandbyModeEvent(HostEvent):
    '''This event records that the host has successfully entered standby mode. A host in
        this mode has no running virtual machines and no provisioning operations
        are occurring.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(EnteredStandbyModeEvent, self).__init__()
    

    
    
