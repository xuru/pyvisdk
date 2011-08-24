
================================================================================
IpPoolIpPoolConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.ip_pool.IpPool`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.ip_pool_ip_pool_config_info.IpPoolIpPoolConfigInfo
    
    .. py:attribute:: dhcpServerAvailable
    
        Whether a DHCP server is available on this network.
        
    
    .. py:attribute:: dns
    
        DNS servers
        
    
    .. py:attribute:: gateway
    
        Gateway. This can be an empty string - if no gateway is configured.
        
    
    .. py:attribute:: ipPoolEnabled
    
        IP addresses can only be allocated from the range if the IP pool is enabled.
        
    
    .. py:attribute:: netmask
    
        Netmask
        
    
    .. py:attribute:: range
    
        IP range. This is specified as a set of ranges separated with commas. One range is given by a start address, a hash (#), and the length of the range.
        
    
    .. py:attribute:: subnetAddress
    
        Address of the subnet.
        
    