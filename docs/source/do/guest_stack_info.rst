
================================================================================
GuestStackInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.guest_info.GuestInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.key_value.KeyValue`,
    :py:class:`~pyvisdk.do.net_dhcp_config_info.NetDhcpConfigInfo`,
    :py:class:`~pyvisdk.do.net_dns_config_info.NetDnsConfigInfo`,
    :py:class:`~pyvisdk.do.net_ip_route_config_info.NetIpRouteConfigInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.guest_stack_info.GuestStackInfo
    
    .. py:attribute:: dhcpConfig
    
        Client side DHCP for a given interface. This reports only the system wide dhcp client settings. See NicInfo.IpConfig for per interface settings. For example on Linux, BSD systems: Using the file dhclient.conf output would be reported as: key='1', value='timeout 60;' key='2', value='reboot 10;'
        
    
    .. py:attribute:: dnsConfig
    
        Client DNS configuration. How DNS queries are resolved.
        
    
    .. py:attribute:: ipRouteConfig
    
        IP route table configuration.
        
    
    .. py:attribute:: ipStackConfig
    
        Report Kernel IP configuration settings. The key part contains a unique number in the report. The value part contains the 'key=value' as provided by the underlying provider. For example on Linux, BSD, the systcl -a output would be reported as: key='5', value='net.ipv4.tcp_keepalive_time = 7200'
        
    