
================================================================================
NetIpConfigSpecIpAddressSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.net_ip_config_spec.NetIpConfigSpec`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_ip_config_spec_ip_address_spec.NetIpConfigSpecIpAddressSpec
    
    .. py:attribute:: ipAddress
    
        IPv4 address is specified using dotted decimal notation. For example, "192.0.2.1". IPv6 addresses are 128-bit addresses specified as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
        
    
    .. py:attribute:: operation
    
        Requires one of: "add" and "remove" or "change" See HostConfigChangeOperation.
        
    
    .. py:attribute:: prefixLength
    
        Denotes the length of a generic Internet network address prefix. The prefix length for IPv4 the value range is 0-32. For IPv6 prefixLength is a decimal value range 0-128. A value of n corresponds to an IP address mask that has n contiguous 1-bits from the most significant bit (MSB), with all other bits set to 0. A value of zero is valid only if the calling context defines it.
        
    