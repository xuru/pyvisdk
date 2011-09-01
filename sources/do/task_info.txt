
================================================================================
TaskInfo
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.post_event.PostEvent`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.task.Task`, :py:class:`~pyvisdk.do.task_event.TaskEvent`,
    :py:class:`~pyvisdk.do.task_history_collector.TaskHistoryCollector`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.localizable_message.LocalizableMessage`,
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`,
    :py:class:`~pyvisdk.do.task.Task`,
    :py:class:`~pyvisdk.do.task_info_state.TaskInfoState`,
    :py:class:`~pyvisdk.do.task_reason.TaskReason`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.create_task.CreateTask`,
    :py:meth:`~pyvisdk.do.read_next_tasks.ReadNextTasks`,
    :py:meth:`~pyvisdk.do.read_previous_tasks.ReadPreviousTasks`
    
.. class:: pyvisdk.do.task_info.TaskInfo
    
    .. py:attribute:: cancelable
    
        Flag to indicate whether or not the cancel task operation is supported.
        
    
    .. py:attribute:: cancelled
    
        Flag to indicate whether or not the client requested cancellation of the task.
        
    
    .. py:attribute:: changeTag
    
        The user entered tag to identify the operations and their side effects
        
    
    .. py:attribute:: completeTime
    
        Time stamp when the task was completed (whether success or failure).
        
    
    .. py:attribute:: description
    
        The description field of the task describes the current phase of operation of the task. For a task that does a single monolithic activity, this will be fixed and unchanging. For tasks that have various substeps, this field will change as the task progresses from one phase to another.
        
    
    .. py:attribute:: descriptionId
    
        An identifier for this operation. This includes publicly visible internal tasks and is a lookup in the TaskDescription methodInfo data object.
        
    
    .. py:attribute:: entity
    
        Managed entity to which the operation applies.
        
    
    .. py:attribute:: entityName
    
        The name of the managed entity, locale-specific, retained for the history collector database.
        
    
    .. py:attribute:: error
    
        If the task state is "error", then this property contains the fault code.
        
    
    .. py:attribute:: eventChainId
    
        Event chain ID that leads to the corresponding events.
        
    
    .. py:attribute:: key
    
        The unique key for the task.
        
    
    .. py:attribute:: locked
    
        If the state of the task is "running", then this property is a list of managed entities that the operation has locked, with a shared lock.
        
    
    .. py:attribute:: name
    
        The name of the operation that created the task. This is not set for internal tasks.
        
    
    .. py:attribute:: parentTaskKey
    
        Tasks can be cretaed by another task. This shows key of the task spun off this task. This is to track causality between tasks.
        
    
    .. py:attribute:: progress
    
        If the task state is "running", then this property contains a progress measurement, expressed as percentage completed, from 0 to 100.
        
    
    .. py:attribute:: queueTime
    
        Time stamp when the task was created.
        
    
    .. py:attribute:: reason
    
        Kind of entity responsible for creating this task.
        
    
    .. py:attribute:: result
    
        If the task state is "success", then this property may be used to hold a return value.
        
    
    .. py:attribute:: rootTaskKey
    
        Tasks can be cretaed by another task and such creation can go on for multiple levels. This is the key of the task that started the chain of tasks.
        
    
    .. py:attribute:: startTime
    
        Time stamp when the task started running.
        
    
    .. py:attribute:: state
    
        Runtime status of the task.
        
    
    .. py:attribute:: task
    
        The managed object that represents this task.
        
    