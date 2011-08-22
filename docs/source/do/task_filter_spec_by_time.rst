
================================================================================
TaskFilterSpecByTime
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.task_filter_spec.TaskFilterSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.task_filter_spec_time_option.TaskFilterSpecTimeOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.task_filter_spec_by_time.TaskFilterSpecByTime
    
    .. py:attribute:: beginTime
    
        The beginning of the time range. If this property is not specified, then tasks are collected from the earliest time in the database.
        
    
    .. py:attribute:: endTime
    
        The end of the time range. If this property is not specified, then tasks are collected up to the latest time in the database.
        
    
    .. py:attribute:: timeType
    
        The time stamp to filter: queued, started, or completed time.
        
    