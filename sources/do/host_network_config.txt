
================================================================================
HostNetworkConfig
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_network_config.UpdateNetworkConfig`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_spec.HostConfigSpec`,
    :py:class:`~pyvisdk.do.host_network_system.HostNetworkSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_dhcp_service_config.HostDhcpServiceConfig`,
    :py:class:`~pyvisdk.do.host_dns_config.HostDnsConfig`,
    :py:class:`~pyvisdk.do.host_ip_route_config.HostIpRouteConfig`,
    :py:class:`~pyvisdk.do.host_ip_route_table_config.HostIpRouteTableConfig`,
    :py:class:`~pyvisdk.do.host_nat_service_config.HostNatServiceConfig`,
    :py:class:`~pyvisdk.do.host_port_group_config.HostPortGroupConfig`,
    :py:class:`~pyvisdk.do.host_proxy_switch_config.HostProxySwitchConfig`,
    :py:class:`~pyvisdk.do.host_virtual_nic_config.HostVirtualNicConfig`,
    :py:class:`~pyvisdk.do.host_virtual_switch_config.HostVirtualSwitchConfig`,
    :py:class:`~pyvisdk.do.physical_nic_config.PhysicalNicConfig`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_network_config.HostNetworkConfig
    
    .. py:attribute:: consoleIpRouteConfig
    
        IP route configuration of the service console.
        
    
    .. py:attribute:: consoleVnic
    
        Virtual network adapters configured for use by the Service Console.
        
    
    .. py:attribute:: dhcp
    
        Dynamic Host Control Protocol (DHCP) Service instances configured on the host.
        
    
    .. py:attribute:: dnsConfig
    
        Client-side DNS configuration for the host. The DNS configuration is global to the entire host.
        
    
    .. py:attribute:: ipRouteConfig
    
        IP route configuration of the host.
        
    
    .. py:attribute:: ipV6Enabled
    
        Enable or disable IPv6 protocol on this system. This property must be set by itself, no other property can accompany this change. Following the successful change, the system should be rebooted to have the change take effect.
        
    
    .. py:attribute:: nat
    
        Network address translation (NAT) Service instances configured on the host.
        
    
    .. py:attribute:: pnic
    
        Physical network adapters as seen by the primary operating system.
        
    
    .. py:attribute:: portgroup
    
        Port groups configured on the host.
        
    
    .. py:attribute:: proxySwitch
    
        Host proxy switches configured on the host.
        
    
    .. py:attribute:: routeTableConfig
    
        IP routing table configuration of the host
        
    
    .. py:attribute:: vnic
    
        Virtual network adapters configured for use by the host operating system network adapter.
        
    
    .. py:attribute:: vswitch
    
        Virtual switches configured on the host.
        
    