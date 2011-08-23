
================================================================================
NetDhcpConfigInfoDhcpOptions
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.net_dhcp_config_info.NetDhcpConfigInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.key_value.KeyValue`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_dhcp_config_info_dhcp_options.NetDhcpConfigInfoDhcpOptions
    
    .. py:attribute:: config
    
        Platform specific settings for DHCP Client. The key part is a unique number, the value part is the platform specific configuration command. For example on Linux, BSD systems using the file dhclient.conf output would be reported at system scope: key='1', value='timeout 60;' key='2', value='reboot 10;' output reported at per interface scope: key='1', value='prepend domain-name-servers 192.0.2.1;' key='2', value='equire subnet-mask, domain-name-servers;'
        
    
    .. py:attribute:: enable
    
        Report state of dhcp client services.
        
    