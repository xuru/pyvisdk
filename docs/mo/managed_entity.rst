

========================================
ManagedEntity
========================================



.. describe:: Property of
    
    :py:class:`~pyvisdk.mo.alarm_info.AlarmInfo`, :py:class:`~pyvisdk.mo.alarm_state.AlarmState`, :py:class:`~pyvisdk.mo.compliance_result.ComplianceResult`, :py:class:`~pyvisdk.mo.container_view.ContainerView`, :py:class:`~pyvisdk.mo.datacenter_mismatch_argument.DatacenterMismatchArgument`, :py:class:`~pyvisdk.mo.distributed_virtual_switch_manager_host_container.DistributedVirtualSwitchManagerHostContainer`, :py:class:`~pyvisdk.mo.distributed_virtual_switch_port_connectee.DistributedVirtualSwitchPortConnectee`, :py:class:`~pyvisdk.mo.distributed_virtual_switch_port_criteria.DistributedVirtualSwitchPortCriteria`, :py:class:`~pyvisdk.mo.dv_port_config_info.DVPortConfigInfo`, :py:class:`~pyvisdk.mo.dv_port_config_spec.DVPortConfigSpec`, :py:class:`~pyvisdk.mo.dv_portgroup_config_info.DVPortgroupConfigInfo`, :py:class:`~pyvisdk.mo.dv_portgroup_config_spec.DVPortgroupConfigSpec`, :py:class:`~pyvisdk.mo.dvs_scope_violated.DvsScopeViolated`, :py:class:`~pyvisdk.mo.event_filter_spec_by_entity.EventFilterSpecByEntity`, :py:class:`~pyvisdk.mo.folder.Folder`, :py:class:`~pyvisdk.mo.http_nfc_lease_info.HttpNfcLeaseInfo`, :py:class:`~pyvisdk.mo.invalid_folder.InvalidFolder`, :py:class:`~pyvisdk.mo.invalid_name.InvalidName`, :py:class:`~pyvisdk.mo.managed_entity.ManagedEntity`, :py:class:`~pyvisdk.mo.managed_entity_event_argument.ManagedEntityEventArgument`, :py:class:`~pyvisdk.mo.permission.Permission`, :py:class:`~pyvisdk.mo.profile.Profile`, :py:class:`~pyvisdk.mo.resource_config_spec.ResourceConfigSpec`, :py:class:`~pyvisdk.mo.scheduled_task_info.ScheduledTaskInfo`, :py:class:`~pyvisdk.mo.task_filter_spec_by_entity.TaskFilterSpecByEntity`, :py:class:`~pyvisdk.mo.task_info.TaskInfo`, :py:class:`~pyvisdk.mo.task_reason_alarm.TaskReasonAlarm`, :py:class:`~pyvisdk.mo.v_app_clone_spec_resource_map.VAppCloneSpecResourceMap`, :py:class:`~pyvisdk.mo.v_app_entity_config_info.VAppEntityConfigInfo`, :py:class:`~pyvisdk.mo.virtual_app.VirtualApp`, :py:class:`~pyvisdk.mo.virtual_app_link_info.VirtualAppLinkInfo`, :py:class:`~pyvisdk.mo.virtual_machine.VirtualMachine`, :py:class:`~pyvisdk.mo.vm_fault_tolerance_config_issue.VmFaultToleranceConfigIssue`, :py:class:`~pyvisdk.mo.vm_fault_tolerance_config_issue_wrapper.VmFaultToleranceConfigIssueWrapper`


.. describe:: Extended by
    
    ComputeResource, Datacenter, Datastore, DistributedVirtualSwitch, Folder, HostSystem, Network, ResourcePool, VirtualMachine


.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.extensible_managed_object.ExtensibleManagedObject`


.. describe:: Returned by
    
    CloseInventoryViewFolder, FindAllByDnsName, FindAllByIp, FindAllByUuid, FindByDnsName, FindByInventoryPath, FindByIp, FindByUuid, FindChild, OpenInventoryViewFolder


.. describe:: Parameter to
    
    AcknowledgeAlarm, AreAlarmActionsEnabled, AssociateProfile, CheckCompliance_Task, CheckProfileCompliance_Task, ClearComplianceStatus, CloseInventoryViewFolder, CreateAlarm, CreateContainerView, CreateDescriptor, CreateScheduledTask, DissociateProfile, EnableAlarmActions, FindAssociatedProfile, FindChild, GetAlarm, GetAlarmState, LogUserEvent, MoveIntoFolder_Task, MoveIntoResourcePool, OpenInventoryViewFolder, QueryCompatibleHostForExistingDvs, QueryCompatibleHostForNewDvs, QueryComplianceStatus, RemoveEntityPermission, ResetEntityPermissions, RetrieveEntityPermissions, RetrieveEntityScheduledTask, SetEntityPermissions, SetField, UpdateLinkedChildren


.. describe:: See also
    
    :py:class:`~pyvisdk.mo.alarm_state.AlarmState`, :py:class:`~pyvisdk.mo.custom_field_value.CustomFieldValue`, :py:class:`~pyvisdk.mo.event.Event`, :py:class:`~pyvisdk.mo.managed_entity_status.ManagedEntityStatus`, :py:class:`~pyvisdk.mo.permission.Permission`, :py:class:`~pyvisdk.mo.tag.Tag`, :py:class:`~pyvisdk.mo.task.Task`


.. autoclass:: pyvisdk.mo.managed_entity.ManagedEntity
    :members:
    :inherited-members:
