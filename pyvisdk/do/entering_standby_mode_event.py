
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EnteringStandbyModeEvent(HostEvent):
    '''This event records that a host has begun the process of entering standby mode. All
        virtual machine operations are blocked, except the following:* MigrateVM *
        PowerOffVM * SuspendVM * ShutdownGuest * StandbyGuest
    '''
    
    def __init__(self, ):
        # MUST define these
        super(EnteringStandbyModeEvent, self).__init__()
    

    
    
