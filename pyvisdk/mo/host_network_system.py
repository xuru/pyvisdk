
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
        information available in NetworkInfo.See HostNetworkInfo'''
        return self.update('networkConfig')
    @property
    def networkInfo(self):
        '''The network configuration and runtime information.'''
        return self.update('networkInfo')
    @property
    def offloadCapabilities(self):
        '''The offload capabilities available on this server.'''
        return self.update('offloadCapabilities')

    
    
    def AddPortGroup(self, portgrp):
        '''Adds a port group to the virtual switch.
        
        :param portgrp: 
        
        '''
        return self.delegate("AddPortGroup")(portgrp)
    
    def AddServiceConsoleVirtualNic(self, portgroup, nic):
        '''Adds a virtual service console network adapter. Returns the device of the
        VirtualNic.Adds a virtual service console network adapter. Returns the device
        of the VirtualNic.
        
        :param portgroup: See usesServiceConsoleNic
        
        :param nic: See usesServiceConsoleNic
        
        '''
        return self.delegate("AddServiceConsoleVirtualNic")(portgroup, nic)
    
    def AddVirtualNic(self, portgroup, nic):
        '''Adds a virtual host/VMkernel network adapter. Returns the device of the virtual
        network adapter.Adds a virtual host/VMkernel network adapter. Returns the
        device of the virtual network adapter.
        
        :param portgroup: Note: Must be the empty string in case nic.distributedVirtualPort is set.
        
        :param nic: 
        
        '''
        return self.delegate("AddVirtualNic")(portgroup, nic)
    
    def AddVirtualSwitch(self, vswitchName, spec=None):
        '''Adds a new virtual switch to the system with the given name. The name must be
        unique with respect to other virtual switches on the host and is limited to 32
        characters.See UpdateVirtualSwitch
        
        :param vswitchName: See UpdateVirtualSwitch
        
        :param spec: See UpdateVirtualSwitch
        
        '''
        return self.delegate("AddVirtualSwitch")(vswitchName, spec)
    
    def QueryNetworkHint(self, device=None):
        '''Requests network hint information for a physical network adapter. A network
        hint is some information about the network to which the physical network
        adapter is attached. The method receives in a list of physical network adapter
        devices and returns an equal number of hints if some devices are provided. If
        the list of devices is empty, then the method accesses hints for all physical
        network adapters.See supportsNetworkHintsSee device
        
        :param device: See supportsNetworkHintsSee device
        
        '''
        return self.delegate("QueryNetworkHint")(device)
    
    def RefreshNetworkSystem(self):
        '''Refresh the network information and settings to pick up any changes that might
        have occurred.
        
        '''
        return self.delegate("RefreshNetworkSystem")()
    
    def RemovePortGroup(self, pgName):
        '''Removes port group from the virtual switch.
        
        :param pgName: 
        
        '''
        return self.delegate("RemovePortGroup")(pgName)
    
    def RemoveServiceConsoleVirtualNic(self, device):
        '''Removes a virtual service console network adapter.See usesServiceConsoleNic
        
        :param device: See usesServiceConsoleNic
        
        '''
        return self.delegate("RemoveServiceConsoleVirtualNic")(device)
    
    def RemoveVirtualNic(self, device):
        '''Removes a virtual host/VMkernel network adapter.
        
        :param device: 
        
        '''
        return self.delegate("RemoveVirtualNic")(device)
    
    def RemoveVirtualSwitch(self, vswitchName):
        '''Removes an existing virtual switch from the system.
        
        :param vswitchName: 
        
        '''
        return self.delegate("RemoveVirtualSwitch")(vswitchName)
    
    def RestartServiceConsoleVirtualNic(self, device):
        '''Restart the service console virtual network adapter interface. If the service
        console virtual network adapter uses DHCP, restarting the interface may result
        it with a different IP configuration, or even fail to be brought up depending
        on the host system network configuration.See usesServiceConsoleNic
        
        :param device: See usesServiceConsoleNic
        
        '''
        return self.delegate("RestartServiceConsoleVirtualNic")(device)
    
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
    
    def UpdateIpRouteConfig(self, config):
        '''Applies the IP route configuration for the host.
        
        :param config: 
        
        '''
        return self.delegate("UpdateIpRouteConfig")(config)
    
    def UpdateIpRouteTableConfig(self, config):
        '''Applies the IP route table configuration for the host.
        
        :param config: 
        
        '''
        return self.delegate("UpdateIpRouteTableConfig")(config)
    
    def UpdateNetworkConfig(self, config, changeMode):
        '''Applies the network configuration. This method operates primarily in two modes:
        <b>replace</b> or <b>modify</b> mode.
        
        :param config: See HostConfigChangeMode
        
        :param changeMode: See HostConfigChangeMode
        
        '''
        return self.delegate("UpdateNetworkConfig")(config, changeMode)
    
    def UpdatePhysicalNicLinkSpeed(self, device, linkSpeed=None):
        '''Configures link speed and duplexity. If linkSpeed is not specified, physical
        network adapter will be set to autonegotiate.See canSetPhysicalNicLinkSpeed
        
        :param device: See canSetPhysicalNicLinkSpeed
        
        :param linkSpeed: See canSetPhysicalNicLinkSpeed
        
        '''
        return self.delegate("UpdatePhysicalNicLinkSpeed")(device, linkSpeed)
    
    def UpdatePortGroup(self, pgName, portgrp):
        '''Reconfigures a port group on the virtual switch.
        
        :param pgName: 
        
        :param portgrp: 
        
        '''
        return self.delegate("UpdatePortGroup")(pgName, portgrp)
    
    def UpdateServiceConsoleVirtualNic(self, device, nic):
        '''Configures the IP configuration for a virtual service console network
        adapter.Configures the IP configuration for a virtual service console network
        adapter.
        
        :param device: See usesServiceConsoleNic
        
        :param nic: See usesServiceConsoleNic
        
        '''
        return self.delegate("UpdateServiceConsoleVirtualNic")(device, nic)
    
    def UpdateVirtualNic(self, device, nic):
        '''Configures virtual host/VMkernel network adapter.Configures virtual
        host/VMkernel network adapter.
        
        :param device: 
        
        :param nic: 
        
        '''
        return self.delegate("UpdateVirtualNic")(device, nic)
    
    def UpdateVirtualSwitch(self, vswitchName, spec):
        '''Updates the properties of the virtual switch.Updates the properties of the
        virtual switch.Updates the properties of the virtual switch.Updates the
        properties of the virtual switch.
        
        :param vswitchName: See HostNicOrderPolicy
        
        :param spec: See HostNicOrderPolicy
        
        '''
        return self.delegate("UpdateVirtualSwitch")(vswitchName, spec)