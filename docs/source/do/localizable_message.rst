
================================================================================
LocalizableMessage
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.set_task_description.SetTaskDescription`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.compliance_failure.ComplianceFailure`,
    :py:class:`~pyvisdk.do.host_profile_manager_config_task_list.HostProfileManagerConfigTaskList`,
    :py:class:`~pyvisdk.do.method_fault.MethodFault`,
    :py:class:`~pyvisdk.do.profile_description_section.ProfileDescriptionSection`,
    :py:class:`~pyvisdk.do.profile_execute_error.ProfileExecuteError`,
    :py:class:`~pyvisdk.do.profile_update_failed_update_failure.ProfileUpdateFailedUpdateFailure`,
    :py:class:`~pyvisdk.do.task_info.TaskInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.key_any_value.KeyAnyValue`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.localizable_message.LocalizableMessage
    
    .. py:attribute:: arg
    
        If the localized message contains variables, messageArg will provide the values for the arguments. e.g: If the message is "IP address is {address}", value for "address" will be provided by #arg.
        
    
    .. py:attribute:: key
    
        Unique key identifying the message in the localized message catalog.
        
    
    .. py:attribute:: message
    
        Message in server locale. This message need not be localized.
        
    