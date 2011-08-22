
================================================================================
TaskFilterSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_collector_for_tasks.CreateCollectorForTasks`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.alarm.Alarm`,
    :py:class:`~pyvisdk.do.scheduled_task.ScheduledTask`,
    :py:class:`~pyvisdk.do.task_filter_spec_by_entity.TaskFilterSpecByEntity`,
    :py:class:`~pyvisdk.do.task_filter_spec_by_time.TaskFilterSpecByTime`,
    :py:class:`~pyvisdk.do.task_filter_spec_by_username.TaskFilterSpecByUsername`,
    :py:class:`~pyvisdk.do.task_info_state.TaskInfoState`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.task_filter_spec.TaskFilterSpec
    
    .. py:attribute:: alarm
    
        This property, if provided, limits the set of collected tasks to those associated with the specified alarm. If not provided, tasks are collected regardless of their association with alarms.
        
    
    .. py:attribute:: entity
    
        The filter specification for retrieving tasks by managed entity. If not provided, then the tasks attached to all managed entities are collected.
        
    
    .. py:attribute:: eventChainId
    
        The filter specification for retrieving tasks by chain ID. If it is set, tasks not with the given eventChainId will be filtered out. If the property is not set, tasks' chain ID is disregarded for filtering purposes.
        
    
    .. py:attribute:: parentTaskKey
    
        The filter specification for retrieving tasks by parentTaskKey. If it is set, tasks not with the given parentTaskKey(s) will be filtered out. If the property is not set, tasks' parentTaskKey is disregarded for filtering purposes.
        
    
    .. py:attribute:: rootTaskKey
    
        The filter specification for retrieving tasks by rootTaskKey. If it is set, tasks not with the given rootTaskKey(s) will be filtered out. If the property is not set, tasks' rootTaskKey is disregarded for filtering purposes.
        
    
    .. py:attribute:: scheduledTask
    
        This property, if provided, limits the set of collected tasks to those associated with the specified scheduled task. If not provided, tasks are collected regardless of their association with any scheduled task.
        
    
    .. py:attribute:: state
    
        This property, if provided, limits the set of collected tasks by their states. Task states are enumerated in State. If not provided, tasks are collected regardless of their state.
        
    
    .. py:attribute:: tag
    
        The filter specification for retrieving tasks by tag. If it is set, tasks not with the given tag(s) will be filtered out. If the property is not set, tasks' tag is disregarded for filtering purposes. If it is set, and includes an empty string, tasks without a tag will be returned.
        
    
    .. py:attribute:: time
    
        The filter specification for retrieving tasks by time. If not provided, then the tasks with any time stamp are collected.
        
    
    .. py:attribute:: userName
    
        The filter specification for retrieving tasks by user name. If not provided, then the tasks belonging to any user are collected.
        
    