
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
    
    

    def UpdatePhysicalNicLinkSpeed(self):
        '''Configures link speed and duplexity. If linkSpeed is not specified, physical
        network adapter will be set to autonegotiate. See
        canSetPhysicalNicLinkSpeed
        '''
        
        return self.delegate("UpdatePhysicalNicLinkSpeed")()
        

    def UpdateNetworkConfig(self):
        '''Applies the network configuration. This method operates primarily in two modes:
        replace or modify mode.

        :rtype: HostNetworkConfigResult 

        '''
        
        return self.delegate("UpdateNetworkConfig")()
        

    def UpdateConsoleIpRouteConfig(self, config):
        '''Applies the IP route configuration for the service console.

        :param config: 

        '''
        
        return self.delegate("UpdateConsoleIpRouteConfig")(config)
        

    def UpdateDnsConfig(self, config):
        '''Applies the client-side DNS configuration for the host.

        :param config: 

        '''
        
        return self.delegate("UpdateDnsConfig")(config)
        

    def UpdateVirtualSwitch(self):
        '''Updates the properties of the virtual switch.If the bridge is NULL, the
        configuration will be unset.If a network adapter is listed in the active
        or standby list, then changing the set of network adapters to which the
        physical network adapter is associated may have a side effect of changing
        the network adapter order policy. If a network adapter is removed from the
        bridge configuration, then the network adapter is removed from the network
        adapter teaming order.The BondBridge configuration is the only valid
        bridge configuration for an ESX Server system. See HostNicOrderPolicy
        '''
        
        return self.delegate("UpdateVirtualSwitch")()
        

    def AddPortGroup(self, portgrp):
        '''Adds a port group to the virtual switch.

        :param portgrp: 

        '''
        
        return self.delegate("AddPortGroup")(portgrp)
        

    def RefreshNetworkSystem(self):
        '''Refresh the network information and settings to pick up any changes that might
        have occurred.
        '''
        
        return self.delegate("RefreshNetworkSystem")()
        

    def UpdateIpRouteTableConfig(self, config):
        '''Applies the IP route table configuration for the host.

        :param config: 

        '''
        
        return self.delegate("UpdateIpRouteTableConfig")(config)
        

    def UpdateServiceConsoleVirtualNic(self):
        '''Configures the IP configuration for a virtual service console network adapter.IP
        configuration is required although it does not have to be enabled if the
        host is an ESX Server system. The dynamic privilege check will check that
        the users have Network.Assign privilege on the DVPortGroup or the DVS if
        the port resides on a DVPortGroup or is a stand-alone DVS port. See
        usesServiceConsoleNic
        '''
        
        return self.delegate("UpdateServiceConsoleVirtualNic")()
        

    def QueryNetworkHint(self):
        '''Requests network hint information for a physical network adapter. A network hint
        is some information about the network to which the physical network
        adapter is attached. The method receives in a list of physical network
        adapter devices and returns an equal number of hints if some devices are
        provided. If the list of devices is empty, then the method accesses hints
        for all physical network adapters. See supportsNetworkHints See device

        :rtype: PhysicalNicHintInfo[] 

        '''
        
        return self.delegate("QueryNetworkHint")()
        

    def RemovePortGroup(self, pgName):
        '''Removes port group from the virtual switch.

        :param pgName: 

        '''
        
        return self.delegate("RemovePortGroup")(pgName)
        

    def RemoveVirtualSwitch(self, vswitchName):
        '''Removes an existing virtual switch from the system.

        :param vswitchName: 

        '''
        
        return self.delegate("RemoveVirtualSwitch")(vswitchName)
        

    def UpdateVirtualNic(self, device, nic):
        '''Configures virtual host/VMkernel network adapter.IP configuration is required
        although it does not have to be enabled if the host is an ESX Server
        system. The dynamic privilege check will ensure that users have
        Host.Config.Network privilege on the host, and Network.Assign privilege on
        the connecting DVPortGroup, or DVS if connecting to a standalone DVPort.
        Network.Assign privilege is not required for operations on standard
        network.

        :param device: 

        :param nic: 

        '''
        
        return self.delegate("UpdateVirtualNic")(device,nic)
        

    def AddServiceConsoleVirtualNic(self):
        '''Adds a virtual service console network adapter. Returns the device of the
        VirtualNic.IP configuration is required although it does not have to be
        enabled if the host is an ESX Server system. The dynamic privilege check
        will ensure that users have Host.Config.Network privilege on the host, and
        Network.Assign privilege on the connecting DVPortGroup, or DVS if
        connecting to a standalone DVPort. Network.Assign privilege is not
        required for operations on standard network. See usesServiceConsoleNic

        :rtype: xsd:string 

        '''
        
        return self.delegate("AddServiceConsoleVirtualNic")()
        

    def UpdatePortGroup(self, pgName, portgrp):
        '''Reconfigures a port group on the virtual switch.

        :param pgName: 

        :param portgrp: 

        '''
        
        return self.delegate("UpdatePortGroup")(pgName,portgrp)
        

    def RemoveVirtualNic(self, device):
        '''Removes a virtual host/VMkernel network adapter.

        :param device: 

        '''
        
        return self.delegate("RemoveVirtualNic")(device)
        

    def AddVirtualSwitch(self):
        '''Adds a new virtual switch to the system with the given name. The name must be
        unique with respect to other virtual switches on the host and is limited
        to 32 characters. See UpdateVirtualSwitch
        '''
        
        return self.delegate("AddVirtualSwitch")()
        

    def RestartServiceConsoleVirtualNic(self):
        '''Restart the service console virtual network adapter interface. If the service
        console virtual network adapter uses DHCP, restarting the interface may
        result it with a different IP configuration, or even fail to be brought up
        depending on the host system network configuration. See
        usesServiceConsoleNic
        '''
        
        return self.delegate("RestartServiceConsoleVirtualNic")()
        

    def AddVirtualNic(self, nic, portgroup):
        '''Adds a virtual host/VMkernel network adapter. Returns the device of the virtual
        network adapter.IP configuration is required although it does not have to
        be enabled if the host is an ESX Server system. The dynamic privilege
        check will ensure that users have Host.Config.Network privilege on the
        host, and Network.Assign privilege on the connecting DVPortGroup, or DVS
        if connecting to a standalone DVPort. Network.Assign privilege is not
        required for operations on standard network.

        :param nic: 

        :param portgroup: 


        :rtype: xsd:string 

        '''
        
        return self.delegate("AddVirtualNic")(nic,portgroup)
        

    def UpdateIpRouteConfig(self, config):
        '''Applies the IP route configuration for the host.

        :param config: 

        '''
        
        return self.delegate("UpdateIpRouteConfig")(config)
        

    def RemoveServiceConsoleVirtualNic(self):
        '''Removes a virtual service console network adapter. See usesServiceConsoleNic
        '''
        
        return self.delegate("RemoveServiceConsoleVirtualNic")()
        
