
================================================================================
HostDhcpServiceSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_dhcp_service.HostDhcpService`,
    :py:class:`~pyvisdk.do.host_dhcp_service_config.HostDhcpServiceConfig`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_dhcp_service_spec.HostDhcpServiceSpec
    
    .. py:attribute:: defaultLeaseDuration
    
        The default DHCP lease duration (minutes).
        
    
    .. py:attribute:: ipSubnetAddr
    
        Subnet served by DHCP service.
        
    
    .. py:attribute:: ipSubnetMask
    
        Subnet mask of network served by DHCP service.
        
    
    .. py:attribute:: leaseBeginIp
    
        The start of the IP address range served by the DHCP service.
        
    
    .. py:attribute:: leaseEndIp
    
        The end of the IP address range served by the DHCP service.
        
    
    .. py:attribute:: maxLeaseDuration
    
        The maximum DHCP lease duration (minutes).
        
    
    .. py:attribute:: unlimitedLease
    
        A flag to indicate whether or not unlimited DHCP lease durations are allowed.
        
    
    .. py:attribute:: virtualSwitch
    
        The name of the virtual switch to which DHCP service is connected.
        
    