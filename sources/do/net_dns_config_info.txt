
================================================================================
NetDnsConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.guest_nic_info.GuestNicInfo`,
    :py:class:`~pyvisdk.do.guest_stack_info.GuestStackInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_dns_config_info.NetDnsConfigInfo
    
    .. py:attribute:: dhcp
    
        Indicates whether or not dynamic host control protocol (DHCP) is used to configure DNS configuration.
        
    
    .. py:attribute:: domainName
    
        The domain name portion of the DNS name. "example.com" part of esx01.example.com.
        
    
    .. py:attribute:: hostName
    
        The host name portion of DNS name. For example, "esx01" part of esx01.example.com.
        
    
    .. py:attribute:: ipAddress
    
        The IP addresses of the DNS servers in order of use. IPv4 addresses are specified using dotted decimal notation. For example, "192.0.2.1". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
        
    
    .. py:attribute:: searchDomain
    
        The domain in which to search for hosts, placed in order of preference.
        
    