
================================================================================
HostListSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_connect_info.HostConnectInfo`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.custom_field_value.CustomFieldValue`,
    :py:class:`~pyvisdk.do.host_config_summary.HostConfigSummary`,
    :py:class:`~pyvisdk.do.host_hardware_summary.HostHardwareSummary`,
    :py:class:`~pyvisdk.do.host_list_summary_quick_stats.HostListSummaryQuickStats`,
    :py:class:`~pyvisdk.do.host_runtime_info.HostRuntimeInfo`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_list_summary.HostListSummary
    
    .. py:attribute:: config
    
        Basic configuration information, if known.
        
    
    .. py:attribute:: currentEVCModeKey
    
        The Enhanced VMotion Compatibility mode that is currently in effect for this host. If the host is in a cluster where EVC is active, this will match the cluster's EVC mode; otherwise this will be unset.See supportedEVCMode
        
    
    .. py:attribute:: customValue
    
        The customized field values.
        
    
    .. py:attribute:: hardware
    
        Basic hardware information, if known.
        
    
    .. py:attribute:: host
    
        The reference to the host-managed object.
        
    
    .. py:attribute:: managementServerIp
    
        IP address of the VirtualCenter server managing this host, if any.
        
    
    .. py:attribute:: maxEVCModeKey
    
        The most capable Enhanced VMotion Compatibility mode supported by the host hardware and software; unset if this host cannot participate in any EVC mode.See supportedEVCMode
        
    
    .. py:attribute:: overallStatus
    
        The overall alarm status of the host.
        
    
    .. py:attribute:: quickStats
    
        Basic host statistics.
        
    
    .. py:attribute:: rebootRequired
    
        Indicates whether or not the host requires a reboot due to a configuration change.
        
    
    .. py:attribute:: runtime
    
        Basic runtime information, if known.
        
    