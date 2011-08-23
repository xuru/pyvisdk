
================================================================================
NetIpRouteConfigInfoIpRoute
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.net_ip_route_config_info.NetIpRouteConfigInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.net_ip_route_config_info_gateway.NetIpRouteConfigInfoGateway`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_ip_route_config_info_ip_route.NetIpRouteConfigInfoIpRoute
    
    .. py:attribute:: gateway
    
        Where to send the packets for this route.
        
    
    .. py:attribute:: network
    
        IP Address of the destination IP network. IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
        
    
    .. py:attribute:: prefixLength
    
        The prefix length. For IPv4 the value range is 0-31. For IPv6 prefixLength is a decimal value range 0-127. The property represents the number of contiguous, higher-order bits of the address that make up the network portion of the IP address.
        
    