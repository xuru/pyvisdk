
================================================================================
HostDnsConfig
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_dns_config.UpdateDnsConfig`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_network_config.HostNetworkConfig`,
    :py:class:`~pyvisdk.do.host_network_info.HostNetworkInfo`,
    :py:class:`~pyvisdk.do.host_network_system.HostNetworkSystem`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.host_dns_config_spec.HostDnsConfigSpec`
    
.. class:: pyvisdk.do.host_dns_config.HostDnsConfig
    
    .. py:attribute:: address
    
        The IP addresses of the DNS servers, placed in order of preference.
        
    
    .. py:attribute:: dhcp
    
        The flag to indicate whether or not DHCP (dynamic host control protocol) is used to determine DNS configuration automatically.
        
    
    .. py:attribute:: domainName
    
        The domain name portion of the DNS name. For example, "vmware.com".
        
    
    .. py:attribute:: hostName
    
        The host name portion of DNS name. For example, "esx01".
        
    
    .. py:attribute:: searchDomain
    
        The domain in which to search for hosts, placed in order of preference.
        
    
    .. py:attribute:: virtualNicDevice
    
        If DHCP is enabled, the DHCP DNS of the service console network adapter will override the system DNS. This field is ignored if DHCP is disabled by the dhcp property.
        
    