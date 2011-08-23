
================================================================================
HostIpConfigIpV6AddressConfiguration
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_ip_config.HostIpConfig`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_ip_config_ip_v6_address.HostIpConfigIpV6Address`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_ip_config_ip_v6_address_configuration.HostIpConfigIpV6AddressConfiguration
    
    .. py:attribute:: autoConfigurationEnabled
    
        Specify if IPv6 address and routing information information be enabled or not as per RFC 2462.
        
    
    .. py:attribute:: dhcpV6Enabled
    
        The flag to indicate whether or not DHCP (dynamic host control protocol) is enabled to obtain an ipV6 address. If this property is set to true, an ipV6 address is configured through dhcpV6.
        
    
    .. py:attribute:: ipV6Address
    
        Ipv6 adrresses configured on the interface. The global addresses can be configured through DHCP, stateless or manual configuration. Link local addresses can be only configured with the origin set to other.
        
    