
================================================================================
TaskScheduler
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.scheduled_task_spec.ScheduledTaskSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.after_startup_task_scheduler.AfterStartupTaskScheduler`,
    :py:class:`~pyvisdk.do.once_task_scheduler.OnceTaskScheduler`,
    :py:class:`~pyvisdk.do.recurrent_task_scheduler.RecurrentTaskScheduler`
    
.. class:: pyvisdk.do.task_scheduler.TaskScheduler
    
    .. py:attribute:: activeTime
    
        The time that the schedule for the task takes effect. Task activation is distinct from task execution. When you activate a task, its schedule starts, and when the next execution time occurs, the task will run. If you do not set activeTime, the activation time defaults to the time that you create the scheduled task.
        
    
    .. py:attribute:: expireTime
    
        The time the schedule for the task expires. If you do not set expireTime, the schedule does not expire.
        
    