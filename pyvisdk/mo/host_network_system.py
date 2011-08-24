
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNetworkSystem(ExtensibleManagedObject):
    '''This managed object type describes networking host configuration and serves as
    the top level container for relevant networking data objects.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostNetworkSystem):
        super(HostNetworkSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def capabilities(self):
        '''Capability vector indicating the available product features.'''
        return self.update('capabilities')
    @property
    def consoleIpRouteConfig(self):
        '''IP route configuration for the service console. The IP route configuration is
    global to the entire host. This property is set only if IP routing can be
    configured for the service console.'''
        return self.update('consoleIpRouteConfig')
    @property
    def dnsConfig(self):
        '''Client-side DNS configuration for the host. The DNS configuration is global to
    the entire host. This is set only if DNS can be configured for the host.'''
        return self.update('dnsConfig')
    @property
    def ipRouteConfig(self):
        '''The IP route configuration for the host. The IP route configuration is global
    to the entire host. This property is set only if IP routing can be configured
    for the host.'''
        return self.update('ipRouteConfig')
    @property
    def networkConfig(self):
        '''Network configuration information. This information can be applied using the
    updateNetworkConfig() method. The information is a strict subset of the
    information available in NetworkInfo.'''
        return self.update('networkConfig')
    @property
    def networkInfo(self):
        '''The network configuration and runtime information.'''
        return self.update('networkInfo')
    @property
    def offloadCapabilities(self):
        '''The offload capabilities available on this server.'''
        return self.update('offloadCapabilities')
    
    
    
    def AddPortGroup(self):
        '''Adds a port group to the virtual switch.
        :rtype: None
        :returns: 
        '''
        return self.delegate("AddPortGroup")()
    
    def AddServiceConsoleVirtualNic(self):
        '''Adds a virtual service console network adapter. Returns the device of the
        VirtualNic.IP configuration is required although it does not have to be enabled
        if the host is an ESX Server system. The dynamic privilege check will ensure
        that users have Host.Config.Network privilege on the host, and Network.Assign
        privilege on the connecting DVPortGroup, or DVS if connecting to a standalone
        DVPort. Network.Assign privilege is not required for operations on standard
        network. See usesServiceConsoleNic
        :rtype: 
        :returns: 
        '''
        return self.delegate("AddServiceConsoleVirtualNic")()
    
    def AddVirtualNic(self):
        '''Adds a virtual host/VMkernel network adapter. Returns the device of the virtual
        network adapter.IP configuration is required although it does not have to be
        enabled if the host is an ESX Server system. The dynamic privilege check will
        ensure that users have Host.Config.Network privilege on the host, and
        Network.Assign privilege on the connecting DVPortGroup, or DVS if connecting to
        a standalone DVPort. Network.Assign privilege is not required for operations on
        standard network.
        :rtype: 
        :returns: 
        '''
        return self.delegate("AddVirtualNic")()
    
    def AddVirtualSwitch(self):
        '''Adds a new virtual switch to the system with the given name. The name must be
        unique with respect to other virtual switches on the host and is limited to 32
        characters. See UpdateVirtualSwitch
        :rtype: None
        :returns: 
        '''
        return self.delegate("AddVirtualSwitch")()
    
    def QueryNetworkHint(self):
        '''Requests network hint information for a physical network adapter. A network
        hint is some information about the network to which the physical network
        adapter is attached. The method receives in a list of physical network adapter
        devices and returns an equal number of hints if some devices are provided. If
        the list of devices is empty, then the method accesses hints for all physical
        network adapters. See supportsNetworkHints See device
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryNetworkHint")()
    
    def RefreshNetworkSystem(self):
        '''Refresh the network information and settings to pick up any changes that might
        have occurred.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RefreshNetworkSystem")()
    
    def RemovePortGroup(self):
        '''Removes port group from the virtual switch.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemovePortGroup")()
    
    def RemoveServiceConsoleVirtualNic(self):
        '''Removes a virtual service console network adapter. See usesServiceConsoleNic
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveServiceConsoleVirtualNic")()
    
    def RemoveVirtualNic(self):
        '''Removes a virtual host/VMkernel network adapter.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveVirtualNic")()
    
    def RemoveVirtualSwitch(self):
        '''Removes an existing virtual switch from the system.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveVirtualSwitch")()
    
    def RestartServiceConsoleVirtualNic(self):
        '''Restart the service console virtual network adapter interface. If the service
        console virtual network adapter uses DHCP, restarting the interface may result
        it with a different IP configuration, or even fail to be brought up depending
        on the host system network configuration. See usesServiceConsoleNic
        :rtype: None
        :returns: 
        '''
        return self.delegate("RestartServiceConsoleVirtualNic")()
    
    def UpdateConsoleIpRouteConfig(self):
        '''Applies the IP route configuration for the service console.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateConsoleIpRouteConfig")()
    
    def UpdateDnsConfig(self):
        '''Applies the client-side DNS configuration for the host.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateDnsConfig")()
    
    def UpdateIpRouteConfig(self):
        '''Applies the IP route configuration for the host.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateIpRouteConfig")()
    
    def UpdateIpRouteTableConfig(self):
        '''Applies the IP route table configuration for the host.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateIpRouteTableConfig")()
    
    def UpdateNetworkConfig(self):
        '''Applies the network configuration. This method operates primarily in two modes:
        replace or modify mode.
        :rtype: 
        :returns: 
        '''
        return self.delegate("UpdateNetworkConfig")()
    
    def UpdatePhysicalNicLinkSpeed(self):
        '''Configures link speed and duplexity. If linkSpeed is not specified, physical
        network adapter will be set to autonegotiate. See canSetPhysicalNicLinkSpeed
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdatePhysicalNicLinkSpeed")()
    
    def UpdatePortGroup(self):
        '''Reconfigures a port group on the virtual switch.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdatePortGroup")()
    
    def UpdateServiceConsoleVirtualNic(self):
        '''Configures the IP configuration for a virtual service console network
        adapter.IP configuration is required although it does not have to be enabled if
        the host is an ESX Server system. The dynamic privilege check will check that
        the users have Network.Assign privilege on the DVPortGroup or the DVS if the
        port resides on a DVPortGroup or is a stand-alone DVS port. See
        usesServiceConsoleNic
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateServiceConsoleVirtualNic")()
    
    def UpdateVirtualNic(self):
        '''Configures virtual host/VMkernel network adapter.IP configuration is required
        although it does not have to be enabled if the host is an ESX Server system.
        The dynamic privilege check will ensure that users have Host.Config.Network
        privilege on the host, and Network.Assign privilege on the connecting
        DVPortGroup, or DVS if connecting to a standalone DVPort. Network.Assign
        privilege is not required for operations on standard network.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateVirtualNic")()
    
    def UpdateVirtualSwitch(self):
        '''Updates the properties of the virtual switch.If the bridge is NULL, the
        configuration will be unset.If a network adapter is listed in the active or
        standby list, then changing the set of network adapters to which the physical
        network adapter is associated may have a side effect of changing the network
        adapter order policy. If a network adapter is removed from the bridge
        configuration, then the network adapter is removed from the network adapter
        teaming order.The BondBridge configuration is the only valid bridge
        configuration for an ESX Server system. See HostNicOrderPolicy
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateVirtualSwitch")()