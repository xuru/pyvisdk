
================================================================================
HostNetCapabilities
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_network_system.HostNetworkSystem`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_net_capabilities.HostNetCapabilities
    
    .. py:attribute:: canSetPhysicalNicLinkSpeed
    
        The flag to indicate whether or not a physical network adapter's link speed and duplex settings can be changed through this API. For a hosted product, the host uses its physical network adapters for network connectivity. Configuration of link speed is done through regular host operations. In ESX Server, the configuration can be changed through this API.
        
    
    .. py:attribute:: dhcpOnVnicSupported
    
        This flag indicates whether or not the host is able to support dhcp configuration for vnics.
        
    
    .. py:attribute:: dnsConfigSupported
    
        The flag to indicate whether DNS configuration for the host is supported.
        
    
    .. py:attribute:: ipRouteConfigSupported
    
        The flag to indicate whether ip route configuration for the host is supported.
        
    
    .. py:attribute:: ipV6Supported
    
        The flag to indicate whether the host is capable of communicating using ipv6 protocol
        
    
    .. py:attribute:: maxPortGroupsPerVswitch
    
        The maximum number of port groups supported per virtual switch. This property will not be set if this value is unlimited.
        
    
    .. py:attribute:: nicTeamingPolicy
    
        The available teaming policies if the platform supports network adapter teaming.
        
    
    .. py:attribute:: supportsNetworkHints
    
        The flag to indicate whether or not the host is able to support the querying of network hints.
        
    
    .. py:attribute:: supportsNicTeaming
    
        The flag to indicate whether or not network adapter teaming is available. Multiple network adapters can be bridged to a virtual switch through a BondBridge. Also, network adapter teaming policies such as failover order and detection are enabled.
        
    
    .. py:attribute:: supportsVlan
    
        The flag to indicate whether or not VLANs can be configured on PortGroups attached to VirtualSwitch objects. This allows VLANs for virtual machines without requiring special VLAN capable hardware switches.
        
    
    .. py:attribute:: usesServiceConsoleNic
    
        The flag to indicate whether or not a service console network adapter is used or required. This means that the system software has two TCP/IP stacks. As a result, at least two types of VirtualNics may be created -- the normal VirtualNic and the service console VirtualNic. If this is not set, then only the VirtualNic type is supported.
        
    
    .. py:attribute:: vnicConfigSupported
    
        The flag to indicate whether vnic configuration is supported. This means that operations to add, remove, update virtualNic are supported.
        
    
    .. py:attribute:: vswitchConfigSupported
    
        The flag to indicate whether virtual switch configuration is supported. This means that operations to add, remove, update virtual switches are supported.
        
    