
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpRouteTableConfig(DynamicData):
    '''IpRouteEntry. Routing entries are individual static routes which combined with the
        default route form all of the routing rules for a host.
    '''
    
    def __init__(self, ipRoute, ipv6Route):
        # MUST define these
        super(HostIpRouteTableConfig, self).__init__()
    
        self.data['ipRoute'] = ipRoute
        self.data['ipv6Route'] = ipv6Route
    
    
    @property
    def ipRoute(self):
        '''The array of Routing ops (routes to be added/removed)
        '''
        return self.data['ipRoute']

    @property
    def ipv6Route(self):
        '''
        '''
        return self.data['ipv6Route']

