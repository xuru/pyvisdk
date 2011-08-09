
from pyvisdk.do.entered_standby_mode_event import EnteredStandbyModeEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DrsEnteredStandbyModeEvent(EnteredStandbyModeEvent):
    '''This event records that the host has successfully entered standby mode initiated
        by Distributed Power Management. A host in this mode has no running
        virtual machines and no provisioning operations are occurring.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(DrsEnteredStandbyModeEvent, self).__init__()
    

    
    
