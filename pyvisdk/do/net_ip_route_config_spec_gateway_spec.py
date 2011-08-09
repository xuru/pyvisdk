
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpRouteConfigSpecGatewaySpec(DynamicData):
    '''IpRoute report an individual host, network or default destination network
        reachable through a given gateway.
    '''
    
    def __init__(self, device, ipAddress):
        # MUST define these
        super(NetIpRouteConfigSpecGatewaySpec, self).__init__()
    
        self.data['device'] = device
        self.data['ipAddress'] = ipAddress
    
    
    @property
    def device(self):
        '''
        '''
        return self.data['device']

    @property
    def ipAddress(self):
        '''
        '''
        return self.data['ipAddress']

