
================================================================================
HostRuntimeInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_list_summary.HostListSummary`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.health_system_runtime.HealthSystemRuntime`,
    :py:class:`~pyvisdk.do.host_system_connection_state.HostSystemConnectionState`,
    :py:class:`~pyvisdk.do.host_system_power_state.HostSystemPowerState`,
    :py:class:`~pyvisdk.do.host_tpm_digest_info.HostTpmDigestInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_runtime_info.HostRuntimeInfo
    
    .. py:attribute:: bootTime
    
        The time when the host was booted.
        
    
    .. py:attribute:: connectionState
    
        The host connection state. See the description in the enums for the ConnectionState data object type.
        
    
    .. py:attribute:: healthSystemRuntime
    
        Available system health status
        
    
    .. py:attribute:: inMaintenanceMode
    
        The flag to indicate whether or not the host is in maintenance mode. This flag is set when the host has entered the maintenance mode. It is not set during the entering phase of maintenance mode.
        
    
    .. py:attribute:: powerState
    
        The host power state. See the description in the enums for the PowerState data object type.
        
    
    .. py:attribute:: standbyMode
    
        The host's standby mode. For valid values see HostStandbyMode. The property is only populated by vCenter server. If queried directly from a ESX host, the property is is unset.
        
    
    .. py:attribute:: tpmPcrValues
    
        The array of PCR digest values stored in the TPM device since the last host boot time.
        
    