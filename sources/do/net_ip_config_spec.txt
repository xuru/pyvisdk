
================================================================================
NetIpConfigSpec
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.net_dhcp_config_spec.NetDhcpConfigSpec`,
    :py:class:`~pyvisdk.do.net_ip_config_spec_ip_address_spec.NetIpConfigSpecIpAddressSpec`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_ip_config_spec.NetIpConfigSpec
    
    .. py:attribute:: autoConfigurationEnabled
    
        Enable or disable ICMPv6 router solictitation requests from a given interface to acquire an IPv6 address and default gateway route from zero, one or more routers on the connected network.
        
    
    .. py:attribute:: dhcp
    
        Configure client side DHCP for a given interface.
        
    
    .. py:attribute:: ipAddress
    
        A set of manual (static) IP addresses to be configured on a given interface.
        
    