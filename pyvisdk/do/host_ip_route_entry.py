
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpRouteEntry(DynamicData):
    '''IpRouteEntry. Routing entries are individual static routes which combined with the
        default route form all of the routing rules for a host.
    '''
    
    def __init__(self, deviceName, gateway, network, prefixLength):
        # MUST define these
        super(HostIpRouteEntry, self).__init__()
    
        self.data['deviceName'] = deviceName
        self.data['gateway'] = gateway
        self.data['network'] = network
        self.data['prefixLength'] = prefixLength
    
    
    @property
    def deviceName(self):
        '''If available the property indicates the device associated with the routing entry.
        This property can only be read from the server. It will be ignored if set
        by the client.
        '''
        return self.data['deviceName']

    @property
    def gateway(self):
        '''Gateway for the routing entry
        '''
        return self.data['gateway']

    @property
    def network(self):
        '''Network of the routing entry Of the format "10.20.120.0" or "2001:db8::1428:57"
        '''
        return self.data['network']

    @property
    def prefixLength(self):
        '''Prefix length of the network (this is the 22 in 10.20.120.0/22)
        '''
        return self.data['prefixLength']

