
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNetworkInfo(DynamicData):
    '''This data object type describes networking host configuration data objects.
    '''
    
    def __init__(self, atBootIpV6Enabled, consoleIpRouteConfig, consoleVnic, dhcp, dnsConfig, ipRouteConfig, ipV6Enabled, nat, pnic, portgroup, proxySwitch, routeTableInfo, vnic, vswitch):
        # MUST define these
        super(HostNetworkInfo, self).__init__()
    
        self.data['atBootIpV6Enabled'] = atBootIpV6Enabled
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
        self.data['routeTableInfo'] = routeTableInfo
        self.data['vnic'] = vnic
        self.data['vswitch'] = vswitch
    
    
    @property
    def atBootIpV6Enabled(self):
        '''If true then dual IPv4/IPv6 stack enabled else IPv4 only.
        '''
        return self.data['atBootIpV6Enabled']

    @property
    def consoleIpRouteConfig(self):
        '''IP route configuration of the service console.
        '''
        return self.data['consoleIpRouteConfig']

    @property
    def consoleVnic(self):
        '''Virtual network adapters configured for use by the service console. The service
        console uses this network access for system management and bootstrapping
        services like network boot. The two sets of virtual network adapters are
        mutually exclusive. A virtual network adapter in this list cannot be used
        for things like VMotion. Likewise, a virtual network adapter in the other
        list cannot be used by the service console.
        '''
        return self.data['consoleVnic']

    @property
    def dhcp(self):
        '''DHCP Service instances configured on the host.
        '''
        return self.data['dhcp']

    @property
    def dnsConfig(self):
        '''Client-side DNS configuration for the host. The DNS configuration is global to the
        entire host. This is set only if DNS is configured for the host.
        '''
        return self.data['dnsConfig']

    @property
    def ipRouteConfig(self):
        '''IP route configuration of the host.
        '''
        return self.data['ipRouteConfig']

    @property
    def ipV6Enabled(self):
        '''Enable or disable IPv6 protocol on this system.
        '''
        return self.data['ipV6Enabled']

    @property
    def nat(self):
        '''NAT service instances configured on the host.
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
        '''Proxy switches configured on the host.
        '''
        return self.data['proxySwitch']

    @property
    def routeTableInfo(self):
        '''IP routing table of the host
        '''
        return self.data['routeTableInfo']

    @property
    def vnic(self):
        '''Virtual network adapters configured on the host (hosted products) or the vmkernel.
        In the hosted architecture, these network adapters are used by the host to
        communicate with the virtual machines running on that host. In the
        VMkernel architecture, these virtual network adapters provide the ESX
        Server with external network access through a virtual switch that is
        bridged to a physical network adapter. The VMkernel uses these network
        adapters for features such as VMotion, NAS, iSCSI, and remote MKS
        connections.
        '''
        return self.data['vnic']

    @property
    def vswitch(self):
        '''Virtual switches configured on the host.
        '''
        return self.data['vswitch']

