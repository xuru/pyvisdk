
from pyvisdk.do.host_ip_route_config import HostIpRouteConfig
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpRouteConfigSpec(HostIpRouteConfig):
    '''Dataobject specifying the configuration for IpRoute
    '''
    
    def __init__(self, gatewayDeviceConnection, ipV6GatewayDeviceConnection):
        # MUST define these
        super(HostIpRouteConfigSpec, self).__init__()
    
        self.data['gatewayDeviceConnection'] = gatewayDeviceConnection
        self.data['ipV6GatewayDeviceConnection'] = ipV6GatewayDeviceConnection
    
    
    @property
    def gatewayDeviceConnection(self):
        '''Choose a gateway device based on what the VirtualNic is connected to. This applies
        to service console gateway only, it is ignored otherwise.
        '''
        return self.data['gatewayDeviceConnection']

    @property
    def ipV6GatewayDeviceConnection(self):
        '''The ipv6 gateway device based on what the VirtualNic is connected to. This applies
        to service console gateway only, it is ignored otherwise.
        '''
        return self.data['ipV6GatewayDeviceConnection']

