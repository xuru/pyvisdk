
================================================================================
HostIpConfigIpV6Address
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_ip_config_ip_v6_address_configuration.HostIpConfigIpV6AddressConfiguration`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_ip_config_ip_v6_address.HostIpConfigIpV6Address
    
    .. py:attribute:: dadState
    
        The state of this ipAddress. Can be one of HostIpConfigIpV6AddressStatus
        
    
    .. py:attribute:: ipAddress
    
        The ipv6 address. When DHCP is enabled, this property reflects the current IP configuration and cannot be set.
        
    
    .. py:attribute:: lifetime
    
        The time when will this address expire. If not set the address lifetime is unlimited.
        
    
    .. py:attribute:: operation
    
        Valid values are "add" and "remove". See HostConfigChangeOperation.
        
    
    .. py:attribute:: origin
    
        The type of the ipv6 address configuration on the interface. This can be one of the types defined my the enum HostIpConfigIpV6AddressConfigType.
        
    
    .. py:attribute:: prefixLength
    
        The prefix length. An ipv6 prefixLength is a decimal value that indicates the number of contiguous, higher-order bits of the address that make up the network portion of the address. For example, 10FA:6604:8136:6502::/64 is a possible IPv6 prefix. The prefix length in this case is 64.
        
    