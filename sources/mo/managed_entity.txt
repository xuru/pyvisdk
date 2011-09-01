
================================================================================
ManagedEntity
================================================================================


**Property of**
    
    :py:class:`~pyvisdk.do.alarm_info.AlarmInfo`,
    :py:class:`~pyvisdk.do.alarm_state.AlarmState`,
    :py:class:`~pyvisdk.do.compliance_result.ComplianceResult`,
    :py:class:`~pyvisdk.do.container_view.ContainerView`,
    :py:class:`~pyvisdk.do.datacenter_mismatch_argument.DatacenterMismatchArgument`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_manager_host_container.DistributedVirtualSwitchManagerHostContainer`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_port_connectee.DistributedVirtualSwitchPortConnectee`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_port_criteria.DistributedVirtualSwitchPortCriteria`,
    :py:class:`~pyvisdk.do.dv_port_config_info.DVPortConfigInfo`,
    :py:class:`~pyvisdk.do.dv_port_config_spec.DVPortConfigSpec`,
    :py:class:`~pyvisdk.do.dv_portgroup_config_info.DVPortgroupConfigInfo`,
    :py:class:`~pyvisdk.do.dv_portgroup_config_spec.DVPortgroupConfigSpec`,
    :py:class:`~pyvisdk.do.dvs_scope_violated.DvsScopeViolated`,
    :py:class:`~pyvisdk.do.event_filter_spec_by_entity.EventFilterSpecByEntity`,
    :py:class:`~pyvisdk.do.folder.Folder`,
    :py:class:`~pyvisdk.do.http_nfc_lease_info.HttpNfcLeaseInfo`,
    :py:class:`~pyvisdk.do.invalid_folder.InvalidFolder`,
    :py:class:`~pyvisdk.do.invalid_name.InvalidName`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`,
    :py:class:`~pyvisdk.do.managed_entity_event_argument.ManagedEntityEventArgument`,
    :py:class:`~pyvisdk.do.permission.Permission`,
    :py:class:`~pyvisdk.do.profile.Profile`,
    :py:class:`~pyvisdk.do.resource_config_spec.ResourceConfigSpec`,
    :py:class:`~pyvisdk.do.scheduled_task_info.ScheduledTaskInfo`,
    :py:class:`~pyvisdk.do.task_filter_spec_by_entity.TaskFilterSpecByEntity`,
    :py:class:`~pyvisdk.do.task_info.TaskInfo`,
    :py:class:`~pyvisdk.do.task_reason_alarm.TaskReasonAlarm`,
    :py:class:`~pyvisdk.do.v_app_clone_spec_resource_map.VAppCloneSpecResourceMap`,
    :py:class:`~pyvisdk.do.v_app_entity_config_info.VAppEntityConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_app.VirtualApp`,
    :py:class:`~pyvisdk.do.virtual_app_link_info.VirtualAppLinkInfo`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`,
    :py:class:`~pyvisdk.do.vm_fault_tolerance_config_issue.VmFaultToleranceConfigIssue`,
    :py:class:`~pyvisdk.do.vm_fault_tolerance_config_issue_wrapper.VmFaultToleranceConfigIssueWrapper`
    
**Extended by**
    
    :py:class:`~pyvisdk.do.compute_resource.ComputeResource`,
    :py:class:`~pyvisdk.do.datacenter.Datacenter`,
    :py:class:`~pyvisdk.do.datastore.Datastore`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch.DistributedVirtualSwitch`,
    :py:class:`~pyvisdk.do.folder.Folder`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.network.Network`,
    :py:class:`~pyvisdk.do.resource_pool.ResourcePool`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
**Extends**
    
    :py:class:`~pyvisdk.mo.extensible_managed_object.ExtensibleManagedObject`
    
**Returned by**
    
    :py:meth:`~pyvisdk.do.close_inventory_view_folder.CloseInventoryViewFolder`,
    :py:meth:`~pyvisdk.do.find_all_by_dns_name.FindAllByDnsName`,
    :py:meth:`~pyvisdk.do.find_all_by_ip.FindAllByIp`,
    :py:meth:`~pyvisdk.do.find_all_by_uuid.FindAllByUuid`,
    :py:meth:`~pyvisdk.do.find_by_dns_name.FindByDnsName`,
    :py:meth:`~pyvisdk.do.find_by_inventory_path.FindByInventoryPath`,
    :py:meth:`~pyvisdk.do.find_by_ip.FindByIp`,
    :py:meth:`~pyvisdk.do.find_by_uuid.FindByUuid`,
    :py:meth:`~pyvisdk.do.find_child.FindChild`,
    :py:meth:`~pyvisdk.do.open_inventory_view_folder.OpenInventoryViewFolder`
    
**Parameter to**
    
    :py:meth:`~pyvisdk.do.acknowledge_alarm.AcknowledgeAlarm`,
    :py:meth:`~pyvisdk.do.are_alarm_actions_enabled.AreAlarmActionsEnabled`,
    :py:meth:`~pyvisdk.do.associate_profile.AssociateProfile`,
    :py:meth:`~pyvisdk.do.check_compliance__task.CheckCompliance_Task`,
    :py:meth:`~pyvisdk.do.check_profile_compliance__task.CheckProfileCompliance_Task`,
    :py:meth:`~pyvisdk.do.clear_compliance_status.ClearComplianceStatus`,
    :py:meth:`~pyvisdk.do.close_inventory_view_folder.CloseInventoryViewFolder`,
    :py:meth:`~pyvisdk.do.create_alarm.CreateAlarm`,
    :py:meth:`~pyvisdk.do.create_container_view.CreateContainerView`,
    :py:meth:`~pyvisdk.do.create_descriptor.CreateDescriptor`,
    :py:meth:`~pyvisdk.do.create_scheduled_task.CreateScheduledTask`,
    :py:meth:`~pyvisdk.do.dissociate_profile.DissociateProfile`,
    :py:meth:`~pyvisdk.do.enable_alarm_actions.EnableAlarmActions`,
    :py:meth:`~pyvisdk.do.find_associated_profile.FindAssociatedProfile`,
    :py:meth:`~pyvisdk.do.find_child.FindChild`,
    :py:meth:`~pyvisdk.do.get_alarm.GetAlarm`,
    :py:meth:`~pyvisdk.do.get_alarm_state.GetAlarmState`,
    :py:meth:`~pyvisdk.do.log_user_event.LogUserEvent`,
    :py:meth:`~pyvisdk.do.move_into_folder__task.MoveIntoFolder_Task`,
    :py:meth:`~pyvisdk.do.move_into_resource_pool.MoveIntoResourcePool`,
    :py:meth:`~pyvisdk.do.open_inventory_view_folder.OpenInventoryViewFolder`,
    :py:meth:`~pyvisdk.do.query_compatible_host_for_existing_dvs.QueryCompatibleHostForExistingDvs`,
    :py:meth:`~pyvisdk.do.query_compatible_host_for_new_dvs.QueryCompatibleHostForNewDvs`,
    :py:meth:`~pyvisdk.do.query_compliance_status.QueryComplianceStatus`,
    :py:meth:`~pyvisdk.do.remove_entity_permission.RemoveEntityPermission`,
    :py:meth:`~pyvisdk.do.reset_entity_permissions.ResetEntityPermissions`,
    :py:meth:`~pyvisdk.do.retrieve_entity_permissions.RetrieveEntityPermissions`,
    :py:meth:`~pyvisdk.do.retrieve_entity_scheduled_task.RetrieveEntityScheduledTask`,
    :py:meth:`~pyvisdk.do.set_entity_permissions.SetEntityPermissions`,
    :py:meth:`~pyvisdk.do.set_field.SetField`,
    :py:meth:`~pyvisdk.do.update_linked_children.UpdateLinkedChildren`
    
**See also**
    
    :py:class:`~pyvisdk.do.alarm_state.AlarmState`,
    :py:class:`~pyvisdk.do.custom_field_value.CustomFieldValue`,
    :py:class:`~pyvisdk.do.event.Event`,
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`,
    :py:class:`~pyvisdk.do.permission.Permission`, :py:class:`~pyvisdk.do.tag.Tag`,
    :py:class:`~pyvisdk.do.task.Task`
    
.. 'autoclass':: pyvisdk.mo.managed_entity.ManagedEntity
    :members:
    :inherited-members: