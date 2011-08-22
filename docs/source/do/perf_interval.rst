
================================================================================
PerfInterval
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_perf_interval.CreatePerfInterval`,
    :py:meth:`~pyvisdk.do.update_perf_interval.UpdatePerfInterval`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.performance_manager.PerformanceManager`,
    :py:class:`~pyvisdk.do.performance_statistics_description.PerformanceStatisticsDescription`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.perf_interval.PerfInterval
    
    .. py:attribute:: enabled
    
        Indicates whether the interval is enabled (true) or disabled (false). Disabling a historical interval prevents vCenter Server from collecting metrics for that interval and all higher (longer) intervals.
        
    
    .. py:attribute:: key
    
        A unique identifier for the interval.
        
    
    .. py:attribute:: length
    
        Number of seconds that the statistics corresponding to this interval are kept on the system.
        
    
    .. py:attribute:: level
    
        Statistics collection level for this historical interval. vCenter Server will aggregate only those statistics that match the value of this property for this historical interval. For ESX, the value of this property is null. For vCenter Server, the value will be a number from 1 to 4.
        
    
    .. py:attribute:: name
    
        The name of the historical interval. A localized string that provides a name for the interval. Names include: * "Past Day" * "Past Week" * "Past Month" * "Past Year" The name is not meaningful in terms of system behavior. That is, the interval named Past Week works as it does because of its length, level, and so on, not because of the value of this string.
        
    
    .. py:attribute:: samplingPeriod
    
        Number of seconds that data is sampled for this interval. The real-time samplingPeriod is 20 seconds.
        
    