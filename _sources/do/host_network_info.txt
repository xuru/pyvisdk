
================================================================================
HostNetworkInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_network_system.HostNetworkSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_dhcp_service.HostDhcpService`,
    :py:class:`~pyvisdk.do.host_dns_config.HostDnsConfig`,
    :py:class:`~pyvisdk.do.host_ip_route_config.HostIpRouteConfig`,
    :py:class:`~pyvisdk.do.host_ip_route_table_info.HostIpRouteTableInfo`,
    :py:class:`~pyvisdk.do.host_nat_service.HostNatService`,
    :py:class:`~pyvisdk.do.host_port_group.HostPortGroup`,
    :py:class:`~pyvisdk.do.host_proxy_switch.HostProxySwitch`,
    :py:class:`~pyvisdk.do.host_virtual_nic.HostVirtualNic`,
    :py:class:`~pyvisdk.do.host_virtual_switch.HostVirtualSwitch`,
    :py:class:`~pyvisdk.do.physical_nic.PhysicalNic`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_network_info.HostNetworkInfo
    
    .. py:attribute:: atBootIpV6Enabled
    
        If true then dual IPv4/IPv6 stack enabled else IPv4 only.
        
    
    .. py:attribute:: consoleIpRouteConfig
    
        IP route configuration of the service console.
        
    
    .. py:attribute:: consoleVnic
    
        Virtual network adapters configured for use by the service console. The service console uses this network access for system management and bootstrapping services like network boot. The two sets of virtual network adapters are mutually exclusive. A virtual network adapter in this list cannot be used for things like VMotion. Likewise, a virtual network adapter in the other list cannot be used by the service console.
        
    
    .. py:attribute:: dhcp
    
        DHCP Service instances configured on the host.
        
    
    .. py:attribute:: dnsConfig
    
        Client-side DNS configuration for the host. The DNS configuration is global to the entire host. This is set only if DNS is configured for the host.
        
    
    .. py:attribute:: ipRouteConfig
    
        IP route configuration of the host.
        
    
    .. py:attribute:: ipV6Enabled
    
        Enable or disable IPv6 protocol on this system.
        
    
    .. py:attribute:: nat
    
        NAT service instances configured on the host.
        
    
    .. py:attribute:: pnic
    
        Physical network adapters as seen by the primary operating system.
        
    
    .. py:attribute:: portgroup
    
        Port groups configured on the host.
        
    
    .. py:attribute:: proxySwitch
    
        Proxy switches configured on the host.
        
    
    .. py:attribute:: routeTableInfo
    
        IP routing table of the host
        
    
    .. py:attribute:: vnic
    
        Virtual network adapters configured on the host (hosted products) or the vmkernel. In the hosted architecture, these network adapters are used by the host to communicate with the virtual machines running on that host. In the VMkernel architecture, these virtual network adapters provide the ESX Server with external network access through a virtual switch that is bridged to a physical network adapter. The VMkernel uses these network adapters for features such as VMotion, NAS, iSCSI, and remote MKS connections.
        
    
    .. py:attribute:: vswitch
    
        Virtual switches configured on the host.
        
    