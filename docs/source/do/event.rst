
================================================================================
Event
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.das_config_fault.DasConfigFault`,
    :py:class:`~pyvisdk.do.event_history_collector.EventHistoryCollector`,
    :py:class:`~pyvisdk.do.event_manager.EventManager`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`,
    :py:class:`~pyvisdk.do.snapshot_revert_issue.SnapshotRevertIssue`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.alarm_event.AlarmEvent`,
    :py:class:`~pyvisdk.do.authorization_event.AuthorizationEvent`,
    :py:class:`~pyvisdk.do.cluster_event.ClusterEvent`,
    :py:class:`~pyvisdk.do.custom_field_event.CustomFieldEvent`,
    :py:class:`~pyvisdk.do.datacenter_event.DatacenterEvent`,
    :py:class:`~pyvisdk.do.datastore_event.DatastoreEvent`,
    :py:class:`~pyvisdk.do.dv_portgroup_event.DVPortgroupEvent`,
    :py:class:`~pyvisdk.do.dvs_event.DvsEvent`,
    :py:class:`~pyvisdk.do.event_ex.EventEx`,
    :py:class:`~pyvisdk.do.general_event.GeneralEvent`,
    :py:class:`~pyvisdk.do.health_status_changed_event.HealthStatusChangedEvent`,
    :py:class:`~pyvisdk.do.host_event.HostEvent`,
    :py:class:`~pyvisdk.do.host_inventory_unreadable_event.HostInventoryUnreadableEvent`,
    :py:class:`~pyvisdk.do.license_event.LicenseEvent`,
    :py:class:`~pyvisdk.do.license_expired_event.LicenseExpiredEvent`,
    :py:class:`~pyvisdk.do.locker_misconfigured_event.LockerMisconfiguredEvent`,
    :py:class:`~pyvisdk.do.locker_reconfigured_event.LockerReconfiguredEvent`,
    :py:class:`~pyvisdk.do.profile_event.ProfileEvent`,
    :py:class:`~pyvisdk.do.resource_pool_event.ResourcePoolEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_event.ScheduledTaskEvent`,
    :py:class:`~pyvisdk.do.session_event.SessionEvent`,
    :py:class:`~pyvisdk.do.task_event.TaskEvent`,
    :py:class:`~pyvisdk.do.template_upgrade_event.TemplateUpgradeEvent`,
    :py:class:`~pyvisdk.do.upgrade_event.UpgradeEvent`,
    :py:class:`~pyvisdk.do.vm_event.VmEvent`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_events.QueryEvents`,
    :py:meth:`~pyvisdk.do.read_next_events.ReadNextEvents`,
    :py:meth:`~pyvisdk.do.read_previous_events.ReadPreviousEvents`,
    :py:meth:`~pyvisdk.do.validate_migration.ValidateMigration`
    
.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.post_event.PostEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.compute_resource_event_argument.ComputeResourceEventArgument`,
    :py:class:`~pyvisdk.do.datacenter_event_argument.DatacenterEventArgument`,
    :py:class:`~pyvisdk.do.datastore_event_argument.DatastoreEventArgument`,
    :py:class:`~pyvisdk.do.dvs_event_argument.DvsEventArgument`,
    :py:class:`~pyvisdk.do.host_event_argument.HostEventArgument`,
    :py:class:`~pyvisdk.do.network_event_argument.NetworkEventArgument`,
    :py:class:`~pyvisdk.do.vm_event_argument.VmEventArgument`
    
.. class:: pyvisdk.do.event.Event
    
    .. py:attribute:: chainId
    
        The parent or group ID.
        
    
    .. py:attribute:: changeTag
    
        The user entered tag to identify the operations and their side effects
        
    
    .. py:attribute:: computeResource
    
        The ComputeResource object of the event.
        
    
    .. py:attribute:: createdTime
    
        The time the event was created.
        
    
    .. py:attribute:: datacenter
    
        The Datacenter object of the event.
        
    
    .. py:attribute:: ds
    
        The Datastore object of the event.
        
    
    .. py:attribute:: dvs
    
        The DistributedVirtualSwitch object of the event.
        
    
    .. py:attribute:: fullFormattedMessage
    
        A formatted text message describing the event. The message may be localized.
        
    
    .. py:attribute:: host
    
        The Host object of the event.
        
    
    .. py:attribute:: key
    
        The event ID.
        
    
    .. py:attribute:: net
    
        The Network object of the event.
        
    
    .. py:attribute:: userName
    
        The user who caused the event.
        
    
    .. py:attribute:: vm
    
        The VirtualMachine object of the event.
        
    