
================================================================================
NetIpConfigInfoIpAddress
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.net_ip_config_info.NetIpConfigInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_ip_config_info_ip_address.NetIpConfigInfoIpAddress
    
    .. py:attribute:: ipAddress
    
        IPv4 address is specified using dotted decimal notation. For example, "192.0.2.1". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
        
    
    .. py:attribute:: lifetime
    
        The time when will this address expire. Durning this time state may change states but is still visible from the network.
        
    
    .. py:attribute:: origin
    
        How this address was configured. This can be one of the values from the enum IpAddressOrigin See IpAddressOrigin for values.
        
    
    .. py:attribute:: prefixLength
    
        Denotes the length of a generic Internet network address prefix. The prefix length for IPv4 the value range is 0-32. For IPv6 prefixLength is a decimal value range 0-128. A value of n corresponds to an IP address mask that has n contiguous 1-bits from the most significant bit (MSB), with all other bits set to 0. A value of zero is valid only if the calling context defines it.
        
    
    .. py:attribute:: state
    
        The state of this ipAddress. Can be one of IpAddressStatus.
        
    