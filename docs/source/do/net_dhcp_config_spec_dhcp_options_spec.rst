
================================================================================
NetDhcpConfigSpecDhcpOptionsSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.net_dhcp_config_spec.NetDhcpConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.key_value.KeyValue`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_dhcp_config_spec_dhcp_options_spec.NetDhcpConfigSpecDhcpOptionsSpec
    
    .. py:attribute:: config
    
        Platform specific settings for DHCP Client. The key part is a unique number, the value part is the platform specific configuration command. See NetDhcpConfigInfo for value formatting.
        
    
    .. py:attribute:: enable
    
        Enable or disable dhcp for IPv4.
        
    
    .. py:attribute:: operation
    
        Requires one of the values from HostConfigChangeOperation.
        
    