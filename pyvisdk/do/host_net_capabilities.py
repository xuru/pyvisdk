
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNetCapabilities(DynamicData):
    '''Capability vector indicating the available product features.
    '''
    
    def __init__(self, canSetPhysicalNicLinkSpeed, dhcpOnVnicSupported, dnsConfigSupported, ipRouteConfigSupported, ipV6Supported, maxPortGroupsPerVswitch, nicTeamingPolicy, supportsNetworkHints, supportsNicTeaming, supportsVlan, usesServiceConsoleNic, vnicConfigSupported, vswitchConfigSupported):
        # MUST define these
        super(HostNetCapabilities, self).__init__()
    
        self.data['canSetPhysicalNicLinkSpeed'] = canSetPhysicalNicLinkSpeed
        self.data['dhcpOnVnicSupported'] = dhcpOnVnicSupported
        self.data['dnsConfigSupported'] = dnsConfigSupported
        self.data['ipRouteConfigSupported'] = ipRouteConfigSupported
        self.data['ipV6Supported'] = ipV6Supported
        self.data['maxPortGroupsPerVswitch'] = maxPortGroupsPerVswitch
        self.data['nicTeamingPolicy'] = nicTeamingPolicy
        self.data['supportsNetworkHints'] = supportsNetworkHints
        self.data['supportsNicTeaming'] = supportsNicTeaming
        self.data['supportsVlan'] = supportsVlan
        self.data['usesServiceConsoleNic'] = usesServiceConsoleNic
        self.data['vnicConfigSupported'] = vnicConfigSupported
        self.data['vswitchConfigSupported'] = vswitchConfigSupported
    
    
    @property
    def canSetPhysicalNicLinkSpeed(self):
        '''The flag to indicate whether or not a physical network adapter's link speed and
        duplex settings can be changed through this API. For a hosted product, the
        host uses its physical network adapters for network connectivity.
        Configuration of link speed is done through regular host operations. In
        ESX Server, the configuration can be changed through this API.
        '''
        return self.data['canSetPhysicalNicLinkSpeed']

    @property
    def dhcpOnVnicSupported(self):
        '''This flag indicates whether or not the host is able to support dhcp configuration
        for vnics.
        '''
        return self.data['dhcpOnVnicSupported']

    @property
    def dnsConfigSupported(self):
        '''The flag to indicate whether DNS configuration for the host is supported.
        '''
        return self.data['dnsConfigSupported']

    @property
    def ipRouteConfigSupported(self):
        '''The flag to indicate whether ip route configuration for the host is supported.
        '''
        return self.data['ipRouteConfigSupported']

    @property
    def ipV6Supported(self):
        '''The flag to indicate whether the host is capable of communicating using ipv6
        protocol
        '''
        return self.data['ipV6Supported']

    @property
    def maxPortGroupsPerVswitch(self):
        '''The maximum number of port groups supported per virtual switch. This property will
        not be set if this value is unlimited.
        '''
        return self.data['maxPortGroupsPerVswitch']

    @property
    def nicTeamingPolicy(self):
        '''The available teaming policies if the platform supports network adapter teaming.
        '''
        return self.data['nicTeamingPolicy']

    @property
    def supportsNetworkHints(self):
        '''The flag to indicate whether or not the host is able to support the querying of
        network hints.
        '''
        return self.data['supportsNetworkHints']

    @property
    def supportsNicTeaming(self):
        '''The flag to indicate whether or not network adapter teaming is available. Multiple
        network adapters can be bridged to a virtual switch through a BondBridge.
        Also, network adapter teaming policies such as failover order and
        detection are enabled.
        '''
        return self.data['supportsNicTeaming']

    @property
    def supportsVlan(self):
        '''The flag to indicate whether or not VLANs can be configured on PortGroups attached
        to VirtualSwitch objects. This allows VLANs for virtual machines without
        requiring special VLAN capable hardware switches.
        '''
        return self.data['supportsVlan']

    @property
    def usesServiceConsoleNic(self):
        '''The flag to indicate whether or not a service console network adapter is used or
        required. This means that the system software has two TCP/IP stacks. As a
        result, at least two types of VirtualNics may be created -- the normal
        VirtualNic and the service console VirtualNic. If this is not set, then
        only the VirtualNic type is supported.
        '''
        return self.data['usesServiceConsoleNic']

    @property
    def vnicConfigSupported(self):
        '''The flag to indicate whether vnic configuration is supported. This means that
        operations to add, remove, update virtualNic are supported.
        '''
        return self.data['vnicConfigSupported']

    @property
    def vswitchConfigSupported(self):
        '''The flag to indicate whether virtual switch configuration is supported. This means
        that operations to add, remove, update virtual switches are supported.
        '''
        return self.data['vswitchConfigSupported']

