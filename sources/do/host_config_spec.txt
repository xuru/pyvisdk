
================================================================================
HostConfigSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.apply_host_config__task.ApplyHostConfig_Task`,
    :py:meth:`~pyvisdk.do.generate_config_task_list.GenerateConfigTaskList`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_profile_manager_config_task_list.HostProfileManagerConfigTaskList`,
    :py:class:`~pyvisdk.do.profile_execute_result.ProfileExecuteResult`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_account_spec.HostAccountSpec`,
    :py:class:`~pyvisdk.do.host_active_directory.HostActiveDirectory`,
    :py:class:`~pyvisdk.do.host_date_time_config.HostDateTimeConfig`,
    :py:class:`~pyvisdk.do.host_firewall_config.HostFirewallConfig`,
    :py:class:`~pyvisdk.do.host_license_spec.HostLicenseSpec`,
    :py:class:`~pyvisdk.do.host_memory_spec.HostMemorySpec`,
    :py:class:`~pyvisdk.do.host_nas_volume_config.HostNasVolumeConfig`,
    :py:class:`~pyvisdk.do.host_network_config.HostNetworkConfig`,
    :py:class:`~pyvisdk.do.host_security_spec.HostSecuritySpec`,
    :py:class:`~pyvisdk.do.host_service_config.HostServiceConfig`,
    :py:class:`~pyvisdk.do.host_storage_device_info.HostStorageDeviceInfo`,
    :py:class:`~pyvisdk.do.host_virtual_nic_manager_nic_type_selection.HostVirtualNicManagerNicTypeSelection`,
    :py:class:`~pyvisdk.do.option_value.OptionValue`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_config_spec.HostConfigSpec
    
    .. py:attribute:: activeDirectory
    
        Active Directory configuration change.
        
    
    .. py:attribute:: datastorePrincipal
    
        Datastore principal user.
        
    
    .. py:attribute:: datastorePrincipalPasswd
    
        Password for the datastore principal.
        
    
    .. py:attribute:: datetime
    
        DateTime Configuration.
        
    
    .. py:attribute:: firewall
    
        Firewall configuration.
        
    
    .. py:attribute:: license
    
        License configuration for the host.
        
    
    .. py:attribute:: memory
    
        Memory configuration for the host.
        
    
    .. py:attribute:: nasDatastore
    
        Configurations to create NAS datastores.
        
    
    .. py:attribute:: network
    
        Network system information.
        
    
    .. py:attribute:: nicTypeSelection
    
        Type selection for different VirtualNics.
        
    
    .. py:attribute:: option
    
        Host configuration options as defined by the OptionValue data object type.
        
    
    .. py:attribute:: security
    
        Security specification.
        
    
    .. py:attribute:: service
    
        Host service configuration.
        
    
    .. py:attribute:: storageDevice
    
        Storage system information.
        
    
    .. py:attribute:: userAccount
    
        List of users to create/update with new password.
        
    
    .. py:attribute:: usergroupAccount
    
        List of users to create/update with new password.
        
    