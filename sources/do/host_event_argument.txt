
================================================================================
HostEventArgument
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.das_host_failed_event.DasHostFailedEvent`,
    :py:class:`~pyvisdk.do.das_host_isolated_event.DasHostIsolatedEvent`,
    :py:class:`~pyvisdk.do.dvs_host_back_in_sync_event.DvsHostBackInSyncEvent`,
    :py:class:`~pyvisdk.do.dvs_host_joined_event.DvsHostJoinedEvent`,
    :py:class:`~pyvisdk.do.dvs_host_left_event.DvsHostLeftEvent`,
    :py:class:`~pyvisdk.do.dvs_host_status_updated.DvsHostStatusUpdated`,
    :py:class:`~pyvisdk.do.dvs_out_of_sync_host_argument.DvsOutOfSyncHostArgument`,
    :py:class:`~pyvisdk.do.event.Event`,
    :py:class:`~pyvisdk.do.host_wwn_conflict_event.HostWwnConflictEvent`,
    :py:class:`~pyvisdk.do.migration_host_error_event.MigrationHostErrorEvent`,
    :py:class:`~pyvisdk.do.migration_host_warning_event.MigrationHostWarningEvent`,
    :py:class:`~pyvisdk.do.migration_resource_error_event.MigrationResourceErrorEvent`,
    :py:class:`~pyvisdk.do.migration_resource_warning_event.MigrationResourceWarningEvent`,
    :py:class:`~pyvisdk.do.vm_being_cloned_event.VmBeingClonedEvent`,
    :py:class:`~pyvisdk.do.vm_being_cloned_no_folder_event.VmBeingClonedNoFolderEvent`,
    :py:class:`~pyvisdk.do.vm_being_hot_migrated_event.VmBeingHotMigratedEvent`,
    :py:class:`~pyvisdk.do.vm_being_migrated_event.VmBeingMigratedEvent`,
    :py:class:`~pyvisdk.do.vm_being_relocated_event.VmBeingRelocatedEvent`,
    :py:class:`~pyvisdk.do.vm_clone_failed_event.VmCloneFailedEvent`,
    :py:class:`~pyvisdk.do.vm_failed_migrate_event.VmFailedMigrateEvent`,
    :py:class:`~pyvisdk.do.vm_migrated_event.VmMigratedEvent`,
    :py:class:`~pyvisdk.do.vm_no_network_access_event.VmNoNetworkAccessEvent`,
    :py:class:`~pyvisdk.do.vm_power_off_on_isolation_event.VmPowerOffOnIsolationEvent`,
    :py:class:`~pyvisdk.do.vm_relocated_event.VmRelocatedEvent`,
    :py:class:`~pyvisdk.do.vm_relocate_failed_event.VmRelocateFailedEvent`,
    :py:class:`~pyvisdk.do.vm_restarted_on_alternate_host_event.VmRestartedOnAlternateHostEvent`,
    :py:class:`~pyvisdk.do.vm_shutdown_on_isolation_event.VmShutdownOnIsolationEvent`,
    :py:class:`~pyvisdk.do.vm_wwn_conflict_event.VmWwnConflictEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.entity_event_argument.EntityEventArgument`
    
.. class:: pyvisdk.do.host_event_argument.HostEventArgument
    
    .. py:attribute:: host
    
        The host object.
        
    