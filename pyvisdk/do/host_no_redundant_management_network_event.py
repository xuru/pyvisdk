
from pyvisdk.do.host_das_event import HostDasEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNoRedundantManagementNetworkEvent(HostDasEvent):
    '''This event records the fact that a host does not have a redundant management
        network. It is recommended that host management networks be configured
        with redundancy.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostNoRedundantManagementNetworkEvent, self).__init__()
    

    
    
