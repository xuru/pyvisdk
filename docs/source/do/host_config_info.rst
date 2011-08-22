
================================================================================
HostConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.about_info.AboutInfo`,
    :py:class:`~pyvisdk.do.datastore.Datastore`,
    :py:class:`~pyvisdk.do.host_authentication_manager_info.HostAuthenticationManagerInfo`,
    :py:class:`~pyvisdk.do.host_auto_start_manager_config.HostAutoStartManagerConfig`,
    :py:class:`~pyvisdk.do.host_datastore_system_capabilities.HostDatastoreSystemCapabilities`,
    :py:class:`~pyvisdk.do.host_date_time_info.HostDateTimeInfo`,
    :py:class:`~pyvisdk.do.host_diagnostic_partition.HostDiagnosticPartition`,
    :py:class:`~pyvisdk.do.host_feature_version_info.HostFeatureVersionInfo`,
    :py:class:`~pyvisdk.do.host_file_system_volume_info.HostFileSystemVolumeInfo`,
    :py:class:`~pyvisdk.do.host_firewall_info.HostFirewallInfo`,
    :py:class:`~pyvisdk.do.host_flag_info.HostFlagInfo`,
    :py:class:`~pyvisdk.do.host_hyper_thread_schedule_info.HostHyperThreadScheduleInfo`,
    :py:class:`~pyvisdk.do.host_ipmi_info.HostIpmiInfo`,
    :py:class:`~pyvisdk.do.host_multipath_state_info.HostMultipathStateInfo`,
    :py:class:`~pyvisdk.do.host_net_capabilities.HostNetCapabilities`,
    :py:class:`~pyvisdk.do.host_net_offload_capabilities.HostNetOffloadCapabilities`,
    :py:class:`~pyvisdk.do.host_network_info.HostNetworkInfo`,
    :py:class:`~pyvisdk.do.host_pci_passthru_info.HostPciPassthruInfo`,
    :py:class:`~pyvisdk.do.host_service_info.HostServiceInfo`,
    :py:class:`~pyvisdk.do.host_ssl_thumbprint_info.HostSslThumbprintInfo`,
    :py:class:`~pyvisdk.do.host_storage_device_info.HostStorageDeviceInfo`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.host_system_resource_info.HostSystemResourceInfo`,
    :py:class:`~pyvisdk.do.host_virtual_nic_manager_info.HostVirtualNicManagerInfo`,
    :py:class:`~pyvisdk.do.host_v_motion_info.HostVMotionInfo`,
    :py:class:`~pyvisdk.do.option_def.OptionDef`,
    :py:class:`~pyvisdk.do.option_value.OptionValue`,
    :py:class:`~pyvisdk.do.power_system_capability.PowerSystemCapability`,
    :py:class:`~pyvisdk.do.power_system_info.PowerSystemInfo`,
    :py:class:`~pyvisdk.do.service_console_reservation_info.ServiceConsoleReservationInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_memory_reservation_info.VirtualMachineMemoryReservationInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_config_info.HostConfigInfo
    
    .. py:attribute:: activeDiagnosticPartition
    
        The diagnostic partition that will be set as the current diagnostic partition on the host.
        
    
    .. py:attribute:: adminDisabled
    
        If the flag is true, the permissions on the host have been modified such that it is only accessible through local console or an authorized centralized management application. This flag is affected by the EnterLockdownMode and ExitLockdownMode operations.
        
    
    .. py:attribute:: authenticationManagerInfo
    
        Current authentication configuration.
        
    
    .. py:attribute:: autoStart
    
        AutoStart configuration.
        
    
    .. py:attribute:: capabilities
    
        Capability vector indicating the available network features.
        
    
    .. py:attribute:: consoleReservation
    
        Memory configuration.
        
    
    .. py:attribute:: datastoreCapabilities
    
        Capability vector indicating available datastore features.
        
    
    .. py:attribute:: datastorePrincipal
    
        Datastore principal user
        
    
    .. py:attribute:: dateTimeInfo
    
        Date/Time related configuration
        
    
    .. py:attribute:: featureVersion
    
        List of feature-specific version information. Each element refers to the version information for a specific feature.
        
    
    .. py:attribute:: fileSystemVolume
    
        Storage system file system volume information.
        
    
    .. py:attribute:: firewall
    
        Firewall configuration.
        
    
    .. py:attribute:: flags
    
        Additional flags for a host.
        
    
    .. py:attribute:: host
    
        A reference to a managed object on a host.
        
    
    .. py:attribute:: hyperThread
    
        If hyperthreading is supported, this is the CPU configuration for optimizing hyperthreading.
        
    
    .. py:attribute:: ipmi
    
        IPMI (Intelligent Platform Management Interface) info for the host.
        
    
    .. py:attribute:: localSwapDatastore
    
        Datastore visible to this host that may be used to store virtual machine swapfiles, for virtual machines executing on this host. The value of this property is set or unset by invoking UpdateLocalSwapDatastore. The policy for using this datastore is determined by the compute resource configuration's vmSwapPlacement property in concert with each individual virtual machine configuration's swapPlacement property.
        
    
    .. py:attribute:: multipathState
    
        Storage multipath state information.
        
    
    .. py:attribute:: network
    
        Network system information.
        
    
    .. py:attribute:: offloadCapabilities
    
        capabilities to offload operations either to the host or to physical hardware when a virtual machine is transmitting on a network
        
    
    .. py:attribute:: option
    
        Host configuration options as defined by the OptionValue data object type.
        
    
    .. py:attribute:: optionDef
    
        A list of supported options.
        
    
    .. py:attribute:: pciPassthruInfo
    
        PCI passthrough information.
        
    
    .. py:attribute:: powerSystemCapability
    
        Host power management capability.
        
    
    .. py:attribute:: powerSystemInfo
    
        Host power management information.
        
    
    .. py:attribute:: product
    
        Information about a product.
        
    
    .. py:attribute:: service
    
        Host service configuration.
        
    
    .. py:attribute:: sslThumbprintInfo
    
        SSL Thumbprint info for hosts in the same cluster
        
    
    .. py:attribute:: storageDevice
    
        Storage system information.
        
    
    .. py:attribute:: systemFile
    
        Datastore paths of files used by the host system on mounted volumes, for instance, the COS vmdk file of the host. For information on datastore paths, see Datastore.
        
    
    .. py:attribute:: systemResources
    
        Reference for the system resource hierarchy, used for configuring the set of resources reserved to the system and unavailable to virtual machines.
        
    
    .. py:attribute:: virtualMachineReservation
    
        Virtual machine memory configuration.
        
    
    .. py:attribute:: virtualNicManagerInfo
    
        VirtualNic manager information.
        
    
    .. py:attribute:: vmotion
    
        VMotion system information.
        
    