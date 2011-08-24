
================================================================================
GuestNicInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.guest_info.GuestInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.net_bios_config_info.NetBIOSConfigInfo`,
    :py:class:`~pyvisdk.do.net_dns_config_info.NetDnsConfigInfo`,
    :py:class:`~pyvisdk.do.net_ip_config_info.NetIpConfigInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.guest_nic_info.GuestNicInfo
    
    .. py:attribute:: connected
    
        Flag indicating whether or not the virtual device is connected.
        
    
    .. py:attribute:: deviceConfigId
    
        Link to the corresponding virtual device.
        
    
    .. py:attribute:: dnsConfig
    
        DNS configuration of the adapter. This property is set only when Guest OS supports it. See StackInfo dnsConfig for system wide settings.
        
    
    .. py:attribute:: ipAddress
    
        
        
    
    .. py:attribute:: ipConfig
    
        IP configuration settings of the adapter See StackInfo ipStackConfig for system wide settings.
        
    
    .. py:attribute:: macAddress
    
        MAC address of the adapter.
        
    
    .. py:attribute:: netBIOSConfig
    
        NetBIOS configuration of the adapter
        
    
    .. py:attribute:: network
    
        Name of the virtual switch portgroup or dvPort connected to this adapter.
        
    