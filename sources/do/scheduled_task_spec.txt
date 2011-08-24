
================================================================================
ScheduledTaskSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_object_scheduled_task.CreateObjectScheduledTask`,
    :py:meth:`~pyvisdk.do.create_scheduled_task.CreateScheduledTask`,
    :py:meth:`~pyvisdk.do.reconfigure_scheduled_task.ReconfigureScheduledTask`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.scheduled_task_info.ScheduledTaskInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.action.Action`,
    :py:class:`~pyvisdk.do.task_scheduler.TaskScheduler`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.scheduled_task_spec.ScheduledTaskSpec
    
    .. py:attribute:: action
    
        The action of the scheduled task, to be done when the scheduled task runs.
        
    
    .. py:attribute:: description
    
        Description of the scheduled task.
        
    
    .. py:attribute:: enabled
    
        Flag to indicate whether the scheduled task is enabled or disabled.
        
    
    .. py:attribute:: name
    
        Name of the scheduled task.
        
    
    .. py:attribute:: notification
    
        The email notification. If not set, this property is set to empty string, indicating no notification.
        
    
    .. py:attribute:: scheduler
    
        The time scheduler that determines when the scheduled task runs.
        
    