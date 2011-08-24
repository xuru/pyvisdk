
================================================================================
ScheduledTaskEvent
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.scheduled_task_completed_event.ScheduledTaskCompletedEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_created_event.ScheduledTaskCreatedEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_email_completed_event.ScheduledTaskEmailCompletedEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_email_failed_event.ScheduledTaskEmailFailedEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_failed_event.ScheduledTaskFailedEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_reconfigured_event.ScheduledTaskReconfiguredEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_removed_event.ScheduledTaskRemovedEvent`,
    :py:class:`~pyvisdk.do.scheduled_task_started_event.ScheduledTaskStartedEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity_event_argument.ManagedEntityEventArgument`,
    :py:class:`~pyvisdk.do.scheduled_task_event_argument.ScheduledTaskEventArgument`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.event.Event`
    
.. class:: pyvisdk.do.scheduled_task_event.ScheduledTaskEvent
    
    .. py:attribute:: entity
    
        The entity on which the scheduled task registered.
        
    
    .. py:attribute:: scheduledTask
    
        The scheduled task object.
        
    