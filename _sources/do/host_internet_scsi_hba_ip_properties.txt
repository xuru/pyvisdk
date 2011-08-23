
================================================================================
HostInternetScsiHbaIPProperties
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_internet_scsi_ip_properties.UpdateInternetScsiIPProperties`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_internet_scsi_hba_ip_properties.HostInternetScsiHbaIPProperties
    
    .. py:attribute:: address
    
        The current IPv4 address.
        
    
    .. py:attribute:: alternateDnsServerAddress
    
        The current secondary DNS address.
        
    
    .. py:attribute:: arpRedirectEnabled
    
        True if ARP Redirect is enabled
        
    
    .. py:attribute:: defaultGateway
    
        The current IPv4 gateway.
        
    
    .. py:attribute:: dhcpConfigurationEnabled
    
        True if the host bus adapter fetches its IP using DHCP.
        
    
    .. py:attribute:: ipv6Address
    
        The current IPv6 address.
        
    
    .. py:attribute:: ipv6DefaultGateway
    
        The current IPv6 default gateway.
        
    
    .. py:attribute:: ipv6SubnetMask
    
        The current IPv6 subnet mask.
        
    
    .. py:attribute:: jumboFramesEnabled
    
        vSphere API 4.0
        
    
    .. py:attribute:: mac
    
        The MAC address.
        
    
    .. py:attribute:: mtu
    
        True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc) Setting enableJumboFrames and not a numeric mtu value implies autoselection of appropriate MTU value for Jumbo Frames.
        
    
    .. py:attribute:: primaryDnsServerAddress
    
        The current primary DNS address.
        
    
    .. py:attribute:: subnetMask
    
        The current IPv4 subnet mask.
        
    