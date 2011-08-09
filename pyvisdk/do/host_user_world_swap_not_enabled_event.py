
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostUserWorldSwapNotEnabledEvent(HostEvent):
    '''This event records that the userworld swap is not enabled on the host. HA needs
        userworld swap to be configured on embedded ESX hosts to function.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostUserWorldSwapNotEnabledEvent, self).__init__()
    

    
    
