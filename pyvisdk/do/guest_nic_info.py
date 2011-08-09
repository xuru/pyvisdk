
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestNicInfo(DynamicData):
    '''
    '''
    
    def __init__(self, connected, deviceConfigId, dnsConfig, ipAddress, ipConfig, macAddress, netBIOSConfig, network):
        # MUST define these
        super(GuestNicInfo, self).__init__()
    
        self.data['connected'] = connected
        self.data['deviceConfigId'] = deviceConfigId
        self.data['dnsConfig'] = dnsConfig
        self.data['ipAddress'] = ipAddress
        self.data['ipConfig'] = ipConfig
        self.data['macAddress'] = macAddress
        self.data['netBIOSConfig'] = netBIOSConfig
        self.data['network'] = network
    
    
    @property
    def connected(self):
        '''Flag indicating whether or not the virtual device is connected.
        '''
        return self.data['connected']

    @property
    def deviceConfigId(self):
        '''Link to the corresponding virtual device.
        '''
        return self.data['deviceConfigId']

    @property
    def dnsConfig(self):
        '''DNS configuration of the adapter. This property is set only when Guest OS supports
        it. See StackInfo dnsConfig for system wide settings.
        '''
        return self.data['dnsConfig']

    @property
    def ipAddress(self):
        '''
        '''
        return self.data['ipAddress']

    @property
    def ipConfig(self):
        '''IP configuration settings of the adapter See StackInfo ipStackConfig for system
        wide settings.
        '''
        return self.data['ipConfig']

    @property
    def macAddress(self):
        '''MAC address of the adapter.
        '''
        return self.data['macAddress']

    @property
    def netBIOSConfig(self):
        '''NetBIOS configuration of the adapter
        '''
        return self.data['netBIOSConfig']

    @property
    def network(self):
        '''Name of the virtual switch portgroup or dvPort connected to this adapter.
        '''
        return self.data['network']

