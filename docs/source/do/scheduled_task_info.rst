
================================================================================
ScheduledTaskInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.scheduled_task.ScheduledTask`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`,
    :py:class:`~pyvisdk.do.scheduled_task.ScheduledTask`,
    :py:class:`~pyvisdk.do.task.Task`,
    :py:class:`~pyvisdk.do.task_info_state.TaskInfoState`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.scheduled_task_spec.ScheduledTaskSpec`
    
.. class:: pyvisdk.do.scheduled_task_info.ScheduledTaskInfo
    
    .. py:attribute:: activeTask
    
        The running task instance when the scheduled task state is "running".
        
    
    .. py:attribute:: entity
    
        The entity on which related events will be logged. If the task is scheduled on a ManagedEntity, this field will also reflect the same ManagedEntity. If task is scheduled on a ManagedObject, this field will have information about the entity on which the events will be logged on behalf of the ManagedObject. ManagedObject itself will be denoted by taskObject
        
    
    .. py:attribute:: error
    
        The fault code when the scheduled task state is "error".
        
    
    .. py:attribute:: lastModifiedTime
    
        The time the scheduled task is created or modified.
        
    
    .. py:attribute:: lastModifiedUser
    
        Last user that modified the scheduled task.
        
    
    .. py:attribute:: nextRunTime
    
        The next time the scheduled task will run.
        
    
    .. py:attribute:: prevRunTime
    
        The last time the scheduled task ran.
        
    
    .. py:attribute:: progress
    
        The task progress when the scheduled task state is "running".
        
    
    .. py:attribute:: result
    
        The operation result when the scheduled task state is "success".
        
    
    .. py:attribute:: scheduledTask
    
        Scheduled task object.
        
    
    .. py:attribute:: state
    
        Scheduled task state.
        
    
    .. py:attribute:: taskObject
    
        The object on which the scheduled task is defined. This field will have information about either the ManagedEntity or the ManagedObject on which the scheduled task is defined.
        
    