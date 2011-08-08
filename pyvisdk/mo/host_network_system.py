
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNetworkSystem(ExtensibleManagedObject):
    '''This managed object type describes networking host configuration and serves as the
        top level container for relevant networking data objects.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostNetworkSystem):
        # MUST define these
        super(HostNetworkSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def capabilities(self):
        '''Capability vector indicating the available product features.
        '''
        return self.update('capabilities')

    @property
    def consoleIpRouteConfig(self):
        '''IP route configuration for the service console. The IP route configuration is
        global to the entire host. This property is set only if IP routing can be
        configured for the service console.
        '''
        return self.update('consoleIpRouteConfig')

    @property
    def dnsConfig(self):
        '''Client-side DNS configuration for the host. The DNS configuration is global to the
        entire host. This is set only if DNS can be configured for the host.
        '''
        return self.update('dnsConfig')

    @property
    def ipRouteConfig(self):
        '''The IP route configuration for the host. The IP route configuration is global to
        the entire host. This property is set only if IP routing can be configured
        for the host.
        '''
        return self.update('ipRouteConfig')

    @property
    def networkConfig(self):
        '''Network configuration information. This information can be applied using the
        updateNetworkConfig() method. The information is a strict subset of the
        information available in NetworkInfo.
        '''
        return self.update('networkConfig')

    @property
    def networkInfo(self):
        '''The network configuration and runtime information.
        '''
        return self.update('networkInfo')

    @property
    def offloadCapabilities(self):
        '''The offload capabilities available on this server.
        '''
        return self.update('offloadCapabilities')


    def AddPortGroup(self):
        '''Adds a port group to the virtual switch.
        '''
        
        return self.delegate("AddPortGroup")()
        

    def AddServiceConsoleVirtualNic(self, portgroup, nic):
        '''Adds a virtual service console network adapter. Returns the device of the
        VirtualNic.IP configuration is required although it does not have to be
        enabled if the host is an ESX Server system. The dynamic privilege check
        will ensure that users have Host.Config.Network privilege on the host, and
        Network.Assign privilege on the connecting DVPortGroup, or DVS if
        connecting to a standalone DVPort. Network.Assign privilege is not
        required for operations on standard network. See usesServiceConsoleNic

        :param portgroup: See usesServiceConsoleNic

        :param nic: See usesServiceConsoleNic


        :rtype: xsd:string 

        '''
        
        return self.delegate("AddServiceConsoleVirtualNic")(portgroup,nic)
        

    def AddVirtualNic(self):
        '''Adds a virtual host/VMkernel network adapter. Returns the device of the virtual
        network adapter.IP configuration is required although it does not have to
        be enabled if the host is an ESX Server system. The dynamic privilege
        check will ensure that users have Host.Config.Network privilege on the
        host, and Network.Assign privilege on the connecting DVPortGroup, or DVS
        if connecting to a standalone DVPort. Network.Assign privilege is not
        required for operations on standard network.

        :rtype: xsd:string 

        '''
        
        return self.delegate("AddVirtualNic")()
        

    def AddVirtualSwitch(self, vswitchName, spec):
        '''Adds a new virtual switch to the system with the given name. The name must be
        unique with respect to other virtual switches on the host and is limited
        to 32 characters. See UpdateVirtualSwitch

        :param vswitchName: See UpdateVirtualSwitch

        :param spec: See UpdateVirtualSwitch

        '''
        
        return self.delegate("AddVirtualSwitch")(vswitchName,spec)
        

    def QueryNetworkHint(self, device):
        '''Requests network hint information for a physical network adapter. A network hint
        is some information about the network to which the physical network
        adapter is attached. The method receives in a list of physical network
        adapter devices and returns an equal number of hints if some devices are
        provided. If the list of devices is empty, then the method accesses hints
        for all physical network adapters. See supportsNetworkHints See device

        :param device: See supportsNetworkHintsSee device


        :rtype: PhysicalNicHintInfo[] 

        '''
        
        return self.delegate("QueryNetworkHint")(device)
        

    def RefreshNetworkSystem(self):
        '''Refresh the network information and settings to pick up any changes that might
        have occurred.
        '''
        
        return self.delegate("RefreshNetworkSystem")()
        

    def RemovePortGroup(self):
        '''Removes port group from the virtual switch.
        '''
        
        return self.delegate("RemovePortGroup")()
        

    def RemoveServiceConsoleVirtualNic(self, device):
        '''Removes a virtual service console network adapter. See usesServiceConsoleNic

        :param device: See usesServiceConsoleNic

        '''
        
        return self.delegate("RemoveServiceConsoleVirtualNic")(device)
        

    def RemoveVirtualNic(self):
        '''Removes a virtual host/VMkernel network adapter.
        '''
        
        return self.delegate("RemoveVirtualNic")()
        

    def RemoveVirtualSwitch(self):
        '''Removes an existing virtual switch from the system.
        '''
        
        return self.delegate("RemoveVirtualSwitch")()
        

    def RestartServiceConsoleVirtualNic(self, device):
        '''Restart the service console virtual network adapter interface. If the service
        console virtual network adapter uses DHCP, restarting the interface may
        result it with a different IP configuration, or even fail to be brought up
        depending on the host system network configuration. See
        usesServiceConsoleNic

        :param device: See usesServiceConsoleNic

        '''
        
        return self.delegate("RestartServiceConsoleVirtualNic")(device)
        

    def UpdateConsoleIpRouteConfig(self):
        '''Applies the IP route configuration for the service console.
        '''
        
        return self.delegate("UpdateConsoleIpRouteConfig")()
        

    def UpdateDnsConfig(self):
        '''Applies the client-side DNS configuration for the host.
        '''
        
        return self.delegate("UpdateDnsConfig")()
        

    def UpdateIpRouteConfig(self):
        '''Applies the IP route configuration for the host.
        '''
        
        return self.delegate("UpdateIpRouteConfig")()
        

    def UpdateIpRouteTableConfig(self):
        '''Applies the IP route table configuration for the host.
        '''
        
        return self.delegate("UpdateIpRouteTableConfig")()
        

    def UpdateNetworkConfig(self, config, changeMode):
        '''Applies the network configuration. This method operates primarily in two modes:
        replace or modify mode.

        :param config: See HostConfigChangeMode

        :param changeMode: See HostConfigChangeMode


        :rtype: HostNetworkConfigResult 

        '''
        
        return self.delegate("UpdateNetworkConfig")(config,changeMode)
        

    def UpdatePhysicalNicLinkSpeed(self, device, linkSpeed):
        '''Configures link speed and duplexity. If linkSpeed is not specified, physical
        network adapter will be set to autonegotiate. See
        canSetPhysicalNicLinkSpeed

        :param device: See canSetPhysicalNicLinkSpeed

        :param linkSpeed: See canSetPhysicalNicLinkSpeed

        '''
        
        return self.delegate("UpdatePhysicalNicLinkSpeed")(device,linkSpeed)
        

    def UpdatePortGroup(self):
        '''Reconfigures a port group on the virtual switch.
        '''
        
        return self.delegate("UpdatePortGroup")()
        

    def UpdateServiceConsoleVirtualNic(self, device, nic):
        '''Configures the IP configuration for a virtual service console network adapter.IP
        configuration is required although it does not have to be enabled if the
        host is an ESX Server system. The dynamic privilege check will check that
        the users have Network.Assign privilege on the DVPortGroup or the DVS if
        the port resides on a DVPortGroup or is a stand-alone DVS port. See
        usesServiceConsoleNic

        :param device: See usesServiceConsoleNic

        :param nic: See usesServiceConsoleNic

        '''
        
        return self.delegate("UpdateServiceConsoleVirtualNic")(device,nic)
        

    def UpdateVirtualNic(self):
        '''Configures virtual host/VMkernel network adapter.IP configuration is required
        although it does not have to be enabled if the host is an ESX Server
        system. The dynamic privilege check will ensure that users have
        Host.Config.Network privilege on the host, and Network.Assign privilege on
        the connecting DVPortGroup, or DVS if connecting to a standalone DVPort.
        Network.Assign privilege is not required for operations on standard
        network.
        '''
        
        return self.delegate("UpdateVirtualNic")()
        

    def UpdateVirtualSwitch(self, vswitchName, spec):
        '''Updates the properties of the virtual switch.If the bridge is NULL, the
        configuration will be unset.If a network adapter is listed in the active
        or standby list, then changing the set of network adapters to which the
        physical network adapter is associated may have a side effect of changing
        the network adapter order policy. If a network adapter is removed from the
        bridge configuration, then the network adapter is removed from the network
        adapter teaming order.The BondBridge configuration is the only valid
        bridge configuration for an ESX Server system. See HostNicOrderPolicy

        :param vswitchName: See HostNicOrderPolicy

        :param spec: See HostNicOrderPolicy

        '''
        
        return self.delegate("UpdateVirtualSwitch")(vswitchName,spec)
        
