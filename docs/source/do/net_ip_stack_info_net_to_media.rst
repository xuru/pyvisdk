
================================================================================
NetIpStackInfoNetToMedia
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.net_ip_stack_info.NetIpStackInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_ip_stack_info_net_to_media.NetIpStackInfoNetToMedia
    
    .. py:attribute:: device
    
        The value will be the name of the interface as reported by the operating system.
        
    
    .. py:attribute:: ipAddress
    
        A Unicast IP address of another system directly reachable w/o routing. IPv4 address is specified using dotted decimal notation. For example, "192.0.2.1". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
        
    
    .. py:attribute:: physicalAddress
    
        The media-dependent of the address or empty string if not yet learned. For Ethernet interfaces this is a MAC address reported in the format: XX:XX:XX:XX:XX:XX where XX are hexadecimal numbers.
        
    
    .. py:attribute:: type
    
        The type/state of this entry as reported by the IP stack. See EntryType for values.
        
    