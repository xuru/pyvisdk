
================================================================================
HostInternetScsiHbaIPCapabilities
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_internet_scsi_hba_ip_capabilities.HostInternetScsiHbaIPCapabilities
    
    .. py:attribute:: addressSettable
    
        True if the host bus adapter supports setting its IP address.
        
    
    .. py:attribute:: alternateDnsServerAddressSettable
    
        True if the host bus adapter supports setting its secondary DNS.
        
    
    .. py:attribute:: arpRedirectSettable
    
        True if the host bus adapter supports setting its ARP Redirect value
        
    
    .. py:attribute:: defaultGatewaySettable
    
        True if the host bus adapter supports setting its gateway.
        
    
    .. py:attribute:: hostNameAsTargetAddress
    
        True if the discovery and static targets can be configured with a host name as opposed to an IP address.
        
    
    .. py:attribute:: ipConfigurationMethodSettable
    
        True if the host bus adapter supports DHCP.
        
    
    .. py:attribute:: ipv6Supported
    
        True if the host bus adapter supports the use of IPv6 addresses
        
    
    .. py:attribute:: mtuSettable
    
        True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc)
        
    
    .. py:attribute:: nameAliasSettable
    
        True if the host bus adapter supports setting its name and alias
        
    
    .. py:attribute:: primaryDnsServerAddressSettable
    
        True if the host bus adapter supports setting its primary DNS.
        
    
    .. py:attribute:: subnetMaskSettable
    
        True if the host bus adapter supports setting its subnet mask.
        
    