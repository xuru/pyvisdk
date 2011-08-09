
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNetworkConfig(DynamicData):
    '''This data object type describes networking host configuration data objects. These
        objects contain only the configuration information for networking. The
        runtime information is available from the NetworkInfo data object type.
        See HostNetworkInfo
    '''
    
    def __init__(self, consoleIpRouteConfig, consoleVnic, dhcp, dnsConfig, ipRouteConfig, ipV6Enabled, nat, pnic, portgroup, proxySwitch, routeTableConfig, vnic, vswitch):
        # MUST define these
        super(HostNetworkConfig, self).__init__()
    
        self.data['consoleIpRouteConfig'] = consoleIpRouteConfig
        self.data['consoleVnic'] = consoleVnic
        self.data['dhcp'] = dhcp
        self.data['dnsConfig'] = dnsConfig
        self.data['ipRouteConfig'] = ipRouteConfig
        self.data['ipV6Enabled'] = ipV6Enabled
        self.data['nat'] = nat
        self.data['pnic'] = pnic
        self.data['portgroup'] = portgroup
        self.data['proxySwitch'] = proxySwitch
        self.data['routeTableConfig'] = routeTableConfig
        self.data['vnic'] = vnic
        self.data['vswitch'] = vswitch
    
    
    @property
    def consoleIpRouteConfig(self):
        '''IP route configuration of the service console.
        '''
        return self.data['consoleIpRouteConfig']

    @property
    def consoleVnic(self):
        '''Virtual network adapters configured for use by the Service Console.
        '''
        return self.data['consoleVnic']

    @property
    def dhcp(self):
        '''Dynamic Host Control Protocol (DHCP) Service instances configured on the host.
        '''
        return self.data['dhcp']

    @property
    def dnsConfig(self):
        '''Client-side DNS configuration for the host. The DNS configuration is global to the
        entire host.
        '''
        return self.data['dnsConfig']

    @property
    def ipRouteConfig(self):
        '''IP route configuration of the host.
        '''
        return self.data['ipRouteConfig']

    @property
    def ipV6Enabled(self):
        '''Enable or disable IPv6 protocol on this system. This property must be set by
        itself, no other property can accompany this change. Following the
        successful change, the system should be rebooted to have the change take
        effect.
        '''
        return self.data['ipV6Enabled']

    @property
    def nat(self):
        '''Network address translation (NAT) Service instances configured on the host.
        '''
        return self.data['nat']

    @property
    def pnic(self):
        '''Physical network adapters as seen by the primary operating system.
        '''
        return self.data['pnic']

    @property
    def portgroup(self):
        '''Port groups configured on the host.
        '''
        return self.data['portgroup']

    @property
    def proxySwitch(self):
        '''Host proxy switches configured on the host.
        '''
        return self.data['proxySwitch']

    @property
    def routeTableConfig(self):
        '''IP routing table configuration of the host
        '''
        return self.data['routeTableConfig']

    @property
    def vnic(self):
        '''Virtual network adapters configured for use by the host operating system network
        adapter.
        '''
        return self.data['vnic']

    @property
    def vswitch(self):
        '''Virtual switches configured on the host.
        '''
        return self.data['vswitch']

