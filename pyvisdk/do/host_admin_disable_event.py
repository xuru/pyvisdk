
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAdminDisableEvent(HostEvent):
    '''This event records that the permission on the host has been changed such that only
        the user account used for VirtualCenter operation will have Administrator
        permission.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostAdminDisableEvent, self).__init__()
    

    
    
