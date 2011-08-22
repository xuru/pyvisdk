
================================================================================
HostConfigManager
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_authentication_manager.HostAuthenticationManager`,
    :py:class:`~pyvisdk.do.host_auto_start_manager.HostAutoStartManager`,
    :py:class:`~pyvisdk.do.host_boot_device_system.HostBootDeviceSystem`,
    :py:class:`~pyvisdk.do.host_cpu_scheduler_system.HostCpuSchedulerSystem`,
    :py:class:`~pyvisdk.do.host_datastore_system.HostDatastoreSystem`,
    :py:class:`~pyvisdk.do.host_date_time_system.HostDateTimeSystem`,
    :py:class:`~pyvisdk.do.host_diagnostic_system.HostDiagnosticSystem`,
    :py:class:`~pyvisdk.do.host_firewall_system.HostFirewallSystem`,
    :py:class:`~pyvisdk.do.host_firmware_system.HostFirmwareSystem`,
    :py:class:`~pyvisdk.do.host_health_status_system.HostHealthStatusSystem`,
    :py:class:`~pyvisdk.do.host_kernel_module_system.HostKernelModuleSystem`,
    :py:class:`~pyvisdk.do.host_memory_system.HostMemorySystem`,
    :py:class:`~pyvisdk.do.host_network_system.HostNetworkSystem`,
    :py:class:`~pyvisdk.do.host_patch_manager.HostPatchManager`,
    :py:class:`~pyvisdk.do.host_pci_passthru_system.HostPciPassthruSystem`,
    :py:class:`~pyvisdk.do.host_power_system.HostPowerSystem`,
    :py:class:`~pyvisdk.do.host_service_system.HostServiceSystem`,
    :py:class:`~pyvisdk.do.host_snmp_system.HostSnmpSystem`,
    :py:class:`~pyvisdk.do.host_storage_system.HostStorageSystem`,
    :py:class:`~pyvisdk.do.host_virtual_nic_manager.HostVirtualNicManager`,
    :py:class:`~pyvisdk.do.host_v_motion_system.HostVMotionSystem`,
    :py:class:`~pyvisdk.do.license_manager.LicenseManager`,
    :py:class:`~pyvisdk.do.option_manager.OptionManager`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_config_manager.HostConfigManager
    
    .. py:attribute:: advancedOption
    
        Advanced options.
        
    
    .. py:attribute:: authenticationManager
    
        Authentication method configuration - for example, for Active Directory membership.
        
    
    .. py:attribute:: autoStartManager
    
        Auto-start and auto-stop configuration.
        
    
    .. py:attribute:: bootDeviceSystem
    
        Boot device order management.
        
    
    .. py:attribute:: cpuScheduler
    
        The CPU scheduler that determines which threads execute on a CPU at any given time.
        
    
    .. py:attribute:: datastoreSystem
    
        The datastore manager.
        
    
    .. py:attribute:: dateTimeSystem
    
        DateTime configuration
        
    
    .. py:attribute:: diagnosticSystem
    
        The diagnostic for the ESX Server system.
        
    
    .. py:attribute:: firewallSystem
    
        The firewall configuration.
        
    
    .. py:attribute:: firmwareSystem
    
        Firmware management.
        
    
    .. py:attribute:: healthStatusSystem
    
        System health status manager.
        
    
    .. py:attribute:: kernelModuleSystem
    
        Kernel module configuration management.
        
    
    .. py:attribute:: licenseManager
    
        License manager
        
    
    .. py:attribute:: memoryManager
    
        The memory manager on the host.
        
    
    .. py:attribute:: networkSystem
    
        The network system configuration.
        
    
    .. py:attribute:: patchManager
    
        Host patch management.
        
    
    .. py:attribute:: pciPassthruSystem
    
        PciDeviceSystem for passthru.
        
    
    .. py:attribute:: powerSystem
    
        Power System manager.
        
    
    .. py:attribute:: serviceSystem
    
        The configuration of the host services (for example, SSH, FTP, and Telnet).
        
    
    .. py:attribute:: snmpSystem
    
        Snmp configuration
        
    
    .. py:attribute:: storageSystem
    
        The storage configuration.
        
    
    .. py:attribute:: virtualNicManager
    
        The VirtualNic configuration.
        
    
    .. py:attribute:: vmotionSystem
    
        The VMotion configuration.
        
    