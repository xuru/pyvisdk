
================================================================================
LocalizedMethodFault
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.alarm_email_failed_event.AlarmEmailFailedEvent`,
    :py:class:`~pyvisdk.do.alarm_script_failed_event.AlarmScriptFailedEvent`,
    :py:class:`~pyvisdk.do.alarm_snmp_failed_event.AlarmSnmpFailedEvent`,
    :py:class:`~pyvisdk.do.cannot_access_vm_config.CannotAccessVmConfig`,
    :py:class:`~pyvisdk.do.cannot_access_vm_disk.CannotAccessVmDisk`,
    :py:class:`~pyvisdk.do.check_result.CheckResult`,
    :py:class:`~pyvisdk.do.cluster_drs_faults_faults_by_vm.ClusterDrsFaultsFaultsByVm`,
    :py:class:`~pyvisdk.do.cluster_not_attempted_vm_info.ClusterNotAttemptedVmInfo`,
    :py:class:`~pyvisdk.do.disallowed_migration_device_attached.DisallowedMigrationDeviceAttached`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_manager_compatibility_result.DistributedVirtualSwitchManagerCompatibilityResult`,
    :py:class:`~pyvisdk.do.drs_resource_configure_failed_event.DrsResourceConfigureFailedEvent`,
    :py:class:`~pyvisdk.do.dvs_operation_bulk_fault_fault_on_host.DvsOperationBulkFaultFaultOnHost`,
    :py:class:`~pyvisdk.do.event_ex.EventEx`,
    :py:class:`~pyvisdk.do.ft_issues_on_host.FtIssuesOnHost`,
    :py:class:`~pyvisdk.do.generic_drs_fault.GenericDrsFault`,
    :py:class:`~pyvisdk.do.host_config_failed.HostConfigFailed`,
    :py:class:`~pyvisdk.do.host_sync_failed_event.HostSyncFailedEvent`,
    :py:class:`~pyvisdk.do.host_unresolved_vmfs_resolution_result.HostUnresolvedVmfsResolutionResult`,
    :py:class:`~pyvisdk.do.host_vmfs_rescan_result.HostVmfsRescanResult`,
    :py:class:`~pyvisdk.do.http_nfc_lease.HttpNfcLease`,
    :py:class:`~pyvisdk.do.incompatible_host_for_ft_secondary.IncompatibleHostForFtSecondary`,
    :py:class:`~pyvisdk.do.migration_event.MigrationEvent`,
    :py:class:`~pyvisdk.do.no_compatible_host.NoCompatibleHost`,
    :py:class:`~pyvisdk.do.ovf_create_descriptor_result.OvfCreateDescriptorResult`,
    :py:class:`~pyvisdk.do.ovf_create_import_spec_result.OvfCreateImportSpecResult`,
    :py:class:`~pyvisdk.do.ovf_parse_descriptor_result.OvfParseDescriptorResult`,
    :py:class:`~pyvisdk.do.ovf_validate_host_result.OvfValidateHostResult`,
    :py:class:`~pyvisdk.do.power_on_ft_secondary_failed.PowerOnFtSecondaryFailed`,
    :py:class:`~pyvisdk.do.scheduled_task_email_failed_event.ScheduledTaskEmailFailedEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_failed_event.ScheduledTaskFailedEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_info.ScheduledTaskInfo`,
    :py:class:`~pyvisdk.do.snapshot_incompatible_device_in_vm.SnapshotIncompatibleDeviceInVm`,
    :py:class:`~pyvisdk.do.task_info.TaskInfo`,
    :py:class:`~pyvisdk.do.template_upgrade_failed_event.TemplateUpgradeFailedEvent`,
    :py:class:`~pyvisdk.do.update_virtual_machine_files_result_failed_vm_file_info.UpdateVirtualMachineFilesResultFailedVmFileInfo`,
    :py:class:`~pyvisdk.do.vm_clone_failed_event.VmCloneFailedEvent`,
    :py:class:`~pyvisdk.do.vm_config_incompatible_for_fault_tolerance.VmConfigIncompatibleForFaultTolerance`,
    :py:class:`~pyvisdk.do.vm_config_incompatible_for_record_replay.VmConfigIncompatibleForRecordReplay`,
    :py:class:`~pyvisdk.do.vm_deploy_failed_event.VmDeployFailedEvent`,
    :py:class:`~pyvisdk.do.vm_disk_failed_event.VmDiskFailedEvent`,
    :py:class:`~pyvisdk.do.vm_failed_migrate_event.VmFailedMigrateEvent`,
    :py:class:`~pyvisdk.do.vm_failed_relayout_event.VmFailedRelayoutEvent`,
    :py:class:`~pyvisdk.do.vm_failed_to_power_off_event.VmFailedToPowerOffEvent`,
    :py:class:`~pyvisdk.do.vm_failed_to_power_on_event.VmFailedToPowerOnEvent`,
    :py:class:`~pyvisdk.do.vm_failed_to_reboot_guest_event.VmFailedToRebootGuestEvent`,
    :py:class:`~pyvisdk.do.vm_failed_to_reset_event.VmFailedToResetEvent`,
    :py:class:`~pyvisdk.do.vm_failed_to_shutdown_guest_event.VmFailedToShutdownGuestEvent`,
    :py:class:`~pyvisdk.do.vm_failed_to_standby_guest_event.VmFailedToStandbyGuestEvent`,
    :py:class:`~pyvisdk.do.vm_failed_to_suspend_event.VmFailedToSuspendEvent`,
    :py:class:`~pyvisdk.do.vm_failover_failed.VmFailoverFailed`,
    :py:class:`~pyvisdk.do.vm_fault_tolerance_config_issue_wrapper.VmFaultToleranceConfigIssueWrapper`,
    :py:class:`~pyvisdk.do.vm_fault_tolerance_op_issues_list.VmFaultToleranceOpIssuesList`,
    :py:class:`~pyvisdk.do.vm_relocate_failed_event.VmRelocateFailedEvent`,
    :py:class:`~pyvisdk.do.vm_secondary_disabled_by_system_event.VmSecondaryDisabledBySystemEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.method_fault.MethodFault`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.localized_method_fault.LocalizedMethodFault
    
    .. py:attribute:: fault
    
        
        
    
    .. py:attribute:: localizedMessage
    
        The localized message that would be sent in the faultstring element of the SOAP Fault. It is optional so that clients are not required to send a localized message to the server, but servers are required to send the localized message to clients.
        
    