
==================================================================================================
NetIpConfigInfoIpAddressOrigin
==================================================================================================

.. describe:: NetIpConfigInfoIpAddressOrigin

    This specifies how an IP address was obtained for a given interface. See RFC 4293 IpAddressOriginTC.
    
    
    .. py:data:: NetIpConfigInfoIpAddressOrigin.dhcp
    
        The address is configured through dhcp.
        
    
    .. py:data:: NetIpConfigInfoIpAddressOrigin.linklayer
    
        The address is obtained through stateless autoconfiguration (autoconf). See RFC 4862, IPv6 Stateless Address Autoconfiguration.
        
    
    .. py:data:: NetIpConfigInfoIpAddressOrigin.manual
    
        The address is configured manually. The term 'static' is a synonym.
        
    
    .. py:data:: NetIpConfigInfoIpAddressOrigin.other
    
        Any other type of address configuration other than the below mentioned ones will fall under this category. For e.g., automatic address configuration for the link local address falls under this type.
        
    
    .. py:data:: NetIpConfigInfoIpAddressOrigin.random
    
        The address is chosen by the system at random e.g., an IPv4 address within 169.254/16, or an RFC 3041 privacy address.
        
    