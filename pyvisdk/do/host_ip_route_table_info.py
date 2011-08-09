
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpRouteTableInfo(DynamicData):
    '''IpRouteTableInfo. This is the list of all static routes on the host
    '''
    
    def __init__(self, ipRoute, ipv6Route):
        # MUST define these
        super(HostIpRouteTableInfo, self).__init__()
    
        self.data['ipRoute'] = ipRoute
        self.data['ipv6Route'] = ipv6Route
    
    
    @property
    def ipRoute(self):
        '''The array of IpRouteEntry
        '''
        return self.data['ipRoute']

    @property
    def ipv6Route(self):
        '''
        '''
        return self.data['ipv6Route']

