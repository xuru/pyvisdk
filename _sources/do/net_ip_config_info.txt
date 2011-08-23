
================================================================================
NetIpConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.guest_nic_info.GuestNicInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.net_dhcp_config_info.NetDhcpConfigInfo`,
    :py:class:`~pyvisdk.do.net_ip_config_info_ip_address.NetIpConfigInfoIpAddress`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_ip_config_info.NetIpConfigInfo
    
    .. py:attribute:: autoConfigurationEnabled
    
        Enable or disable ICMPv6 router solictitation requests from a given interface to acquire an IPv6 address and default gateway route from zero, one or more routers on the connected network. If not set then ICMPv6 is not available on this system, See vim.host.Network.Capabilities
        
    
    .. py:attribute:: dhcp
    
        Client side DHCP for a given interface.
        
    
    .. py:attribute:: ipAddress
    
        Zero, one or more manual (static) assigned IP addresses to be configured on a given interface.
        
    