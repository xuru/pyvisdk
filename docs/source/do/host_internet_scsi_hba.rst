
================================================================================
HostInternetScsiHba
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_authentication_capabilities.HostInternetScsiHbaAuthenticationCapabilities`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_authentication_properties.HostInternetScsiHbaAuthenticationProperties`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_digest_capabilities.HostInternetScsiHbaDigestCapabilities`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_digest_properties.HostInternetScsiHbaDigestProperties`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_discovery_capabilities.HostInternetScsiHbaDiscoveryCapabilities`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_discovery_properties.HostInternetScsiHbaDiscoveryProperties`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_ip_capabilities.HostInternetScsiHbaIPCapabilities`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_ip_properties.HostInternetScsiHbaIPProperties`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_param_value.HostInternetScsiHbaParamValue`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_send_target.HostInternetScsiHbaSendTarget`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_static_target.HostInternetScsiHbaStaticTarget`,
    :py:class:`~pyvisdk.do.option_def.OptionDef`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.host_host_bus_adapter.HostHostBusAdapter`
    
.. class:: pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba
    
    .. py:attribute:: advancedOptions
    
        A list of the current options settings for the host bus adapter.
        
    
    .. py:attribute:: authenticationCapabilities
    
        The authentication capabilities for this host bus adapter.
        
    
    .. py:attribute:: authenticationProperties
    
        The authentication settings for this host bus adapter. All static and discovery targets will inherit the use of these settings unless their authentication settings are explicitly set.
        
    
    .. py:attribute:: configuredSendTarget
    
        The configured iSCSI send target entries.
        
    
    .. py:attribute:: configuredStaticTarget
    
        The configured iSCSI static target entries.
        
    
    .. py:attribute:: currentSpeedMb
    
        The Current operating link speed of the port in megabits per second.
        
    
    .. py:attribute:: digestCapabilities
    
        The authentication capabilities for this host bus adapter.
        
    
    .. py:attribute:: digestProperties
    
        The digest settings for this host bus adapter. All static and discovery targets will inherit the use of these properties unless their digest settings are explicitly set.
        
    
    .. py:attribute:: discoveryCapabilities
    
        The discovery capabilities for this host bus adapter.
        
    
    .. py:attribute:: discoveryProperties
    
        The discovery settings for this host bus adapter.
        
    
    .. py:attribute:: ipCapabilities
    
        The IP capabilities for this host bus adapter.
        
    
    .. py:attribute:: ipProperties
    
        The IP settings for this host bus adapter.
        
    
    .. py:attribute:: iScsiAlias
    
        The iSCSI alias of this host bus adapter.
        
    
    .. py:attribute:: iScsiName
    
        The iSCSI name of this host bus adapter.
        
    
    .. py:attribute:: isSoftwareBased
    
        True if this host bus adapter is a software based initiator utilizing the hosting system's existing TCP/IP network connection
        
    
    .. py:attribute:: maxSpeedMb
    
        The maximum supported link speed of the port in megabits per second.
        
    
    .. py:attribute:: supportedAdvancedOptions
    
        A list of supported key/value pair advanced options for the host bus adapter including their type information.
        
    