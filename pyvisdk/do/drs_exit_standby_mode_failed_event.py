
from pyvisdk.do.exit_standby_mode_failed_event import ExitStandbyModeFailedEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DrsExitStandbyModeFailedEvent(ExitStandbyModeFailedEvent):
    '''This event records that Distributed Power Managment tried to bring a host out from
        standby mode, but the host failed to exit standby mode.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(DrsExitStandbyModeFailedEvent, self).__init__()
    

    
    
