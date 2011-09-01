
================================================================================
ServiceContent
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.service_instance.ServiceInstance`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.about_info.AboutInfo`,
    :py:class:`~pyvisdk.do.alarm_manager.AlarmManager`,
    :py:class:`~pyvisdk.do.authorization_manager.AuthorizationManager`,
    :py:class:`~pyvisdk.do.cluster_profile_manager.ClusterProfileManager`,
    :py:class:`~pyvisdk.do.custom_fields_manager.CustomFieldsManager`,
    :py:class:`~pyvisdk.do.customization_spec_manager.CustomizationSpecManager`,
    :py:class:`~pyvisdk.do.diagnostic_manager.DiagnosticManager`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_manager.DistributedVirtualSwitchManager`,
    :py:class:`~pyvisdk.do.event_manager.EventManager`,
    :py:class:`~pyvisdk.do.extension_manager.ExtensionManager`,
    :py:class:`~pyvisdk.do.file_manager.FileManager`,
    :py:class:`~pyvisdk.do.folder.Folder`,
    :py:class:`~pyvisdk.do.host_local_account_manager.HostLocalAccountManager`,
    :py:class:`~pyvisdk.do.host_profile_manager.HostProfileManager`,
    :py:class:`~pyvisdk.do.host_snmp_system.HostSnmpSystem`,
    :py:class:`~pyvisdk.do.ip_pool_manager.IpPoolManager`,
    :py:class:`~pyvisdk.do.license_manager.LicenseManager`,
    :py:class:`~pyvisdk.do.localization_manager.LocalizationManager`,
    :py:class:`~pyvisdk.do.option_manager.OptionManager`,
    :py:class:`~pyvisdk.do.ovf_manager.OvfManager`,
    :py:class:`~pyvisdk.do.performance_manager.PerformanceManager`,
    :py:class:`~pyvisdk.do.profile_compliance_manager.ProfileComplianceManager`,
    :py:class:`~pyvisdk.do.property_collector.PropertyCollector`,
    :py:class:`~pyvisdk.do.scheduled_task_manager.ScheduledTaskManager`,
    :py:class:`~pyvisdk.do.search_index.SearchIndex`,
    :py:class:`~pyvisdk.do.session_manager.SessionManager`,
    :py:class:`~pyvisdk.do.storage_resource_manager.StorageResourceManager`,
    :py:class:`~pyvisdk.do.task_manager.TaskManager`,
    :py:class:`~pyvisdk.do.user_directory.UserDirectory`,
    :py:class:`~pyvisdk.do.view_manager.ViewManager`,
    :py:class:`~pyvisdk.do.virtual_disk_manager.VirtualDiskManager`,
    :py:class:`~pyvisdk.do.virtualization_manager.VirtualizationManager`,
    :py:class:`~pyvisdk.do.virtual_machine_compatibility_checker.VirtualMachineCompatibilityChecker`,
    :py:class:`~pyvisdk.do.virtual_machine_provisioning_checker.VirtualMachineProvisioningChecker`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.retrieve_service_content.RetrieveServiceContent`
    
.. class:: pyvisdk.do.service_content.ServiceContent
    
    .. py:attribute:: about
    
        Information about the service, such as the software version.
        
    
    .. py:attribute:: accountManager
    
        A singleton managed object that manages host local user and group accounts.
        
    
    .. py:attribute:: alarmManager
    
        A singleton managed object that manages alarms.
        
    
    .. py:attribute:: authorizationManager
    
        Manages permissions for managed entities in the service.
        
    
    .. py:attribute:: clusterProfileManager
    
        A singleton managed object that manages the cluster profiles.
        
    
    .. py:attribute:: complianceManager
    
        A singleton managed object that manages compliance aspects of entities.
        
    
    .. py:attribute:: customFieldsManager
    
        A singleton managed object that managed custom fields.
        
    
    .. py:attribute:: customizationSpecManager
    
        A singleton managed object that manages saved guest customization specifications.
        
    
    .. py:attribute:: diagnosticManager
    
        A singleton managed object that provides access to low-level log files.
        
    
    .. py:attribute:: dvSwitchManager
    
        A singleton managed object that provides relevant information of DistributedVirtualSwitch.
        
    
    .. py:attribute:: eventManager
    
        A singleton managed object that manages events.
        
    
    .. py:attribute:: extensionManager
    
        A singleton managed object that manages extensions.
        
    
    .. py:attribute:: fileManager
    
        A singleton managed object that allows management of files present on datastores.
        
    
    .. py:attribute:: hostProfileManager
    
        A singleton managed object that manages the host profiles.
        
    
    .. py:attribute:: ipPoolManager
    
        A singleton managed object that supports management of IpPool objects. IP pools are used when allocating IPv4 and IPv6 addresses to vApps.
        
    
    .. py:attribute:: licenseManager
    
        A singleton managed object that manages licensing
        
    
    .. py:attribute:: localizationManager
    
        A singleton managed object that provides methods for retrieving message catalogs for client-side localization support.
        
    
    .. py:attribute:: ovfManager
    
        A singleton managed object that can generate OVF descriptors (export) and create vApps (single-VM or vApp container-based) from OVF descriptors (import).
        
    
    .. py:attribute:: perfManager
    
        A singleton managed object that manages the collection and reporting of performance statistics.
        
    
    .. py:attribute:: propertyCollector
    
        Reference to a per-session object for retrieving properties and updates.
        
    
    .. py:attribute:: rootFolder
    
        Reference to the top of the inventory managed by this service.
        
    
    .. py:attribute:: scheduledTaskManager
    
        A singleton managed object that manages scheduled tasks.
        
    
    .. py:attribute:: searchIndex
    
        A singleton managed object that allows search of the inventory
        
    
    .. py:attribute:: sessionManager
    
        Managed object for logging in and managing sessions.
        
    
    .. py:attribute:: setting
    
        Generic configuration for a management server. This is for example by vCenter to store the vCenter Settings. This is not used for a stand-alone host, instead the vim.host.ConfigManager.advancedOption is used.See HostConfigManager
        
    
    .. py:attribute:: snmpSystem
    
        A singleton managed object that allows SNMP configuration. Not set if not supported on a particular platform.
        
    
    .. py:attribute:: storageResourceManager
    
        A singleton managed object that provides methods for storage resource management.
        
    
    .. py:attribute:: taskManager
    
        A singleton managed object that manages tasks.
        
    
    .. py:attribute:: userDirectory
    
        A user directory managed object.
        
    
    .. py:attribute:: viewManager
    
        A singleton managed object for tracking custom sets of objects.
        
    
    .. py:attribute:: virtualDiskManager
    
        A singleton managed object that allows management of virtual disks on datastores.
        
    
    .. py:attribute:: virtualizationManager
    
        A singleton managed object that manages the discovery, analysis, recommendation and virtualization of physical machines
        
    
    .. py:attribute:: vmCompatibilityChecker
    
        A singleton managed object that can answer questions about compatibility of a virtual machine with a host.
        
    
    .. py:attribute:: vmProvisioningChecker
    
        A singleton managed object that can answer questions about the feasibility of certain provisioning operations.
        
    