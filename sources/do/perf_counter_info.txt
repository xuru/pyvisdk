
================================================================================
PerfCounterInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.performance_manager.PerformanceManager`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.element_description.ElementDescription`,
    :py:class:`~pyvisdk.do.perf_stats_type.PerfStatsType`,
    :py:class:`~pyvisdk.do.perf_summary_type.PerfSummaryType`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_perf_counter.QueryPerfCounter`,
    :py:meth:`~pyvisdk.do.query_perf_counter_by_level.QueryPerfCounterByLevel`
    
.. class:: pyvisdk.do.perf_counter_info.PerfCounterInfo
    
    .. py:attribute:: associatedCounterId
    
        The counter IDs associated with the same performance counter name for the same device type. For example, the rollup types for CPU Usage for a host are average, minimum, and maximum. Therefore, their counter IDs are associated.
        
    
    .. py:attribute:: groupInfo
    
        The group of the performance counter with its label and summary details. Counter groups include "cpu," "mem," "net," "disk," "system," "rescpu," and "clusterServices," for example.
        
    
    .. py:attribute:: key
    
        A system-generated number that uniquely identifies the counter in the context of the system. The performance counter ID.
        
    
    .. py:attribute:: level
    
        Minimum level at which metrics of this type will be collected by VirtualCenter Server. The value for this property for any performance counter is a number from 1 to 4. The higher the setting, the more data is collected by VirtualCenter Server. The default setting for VirtualCenter Server is 1, which collects the minimal amount of performance data that is typically useful to administrators and developers alike. The specific level of each counter is documented in the respective counter-documentation pages, by group. See PerformanceManager for links to the counter group pages.
        
    
    .. py:attribute:: nameInfo
    
        The name of the counter with label and summary details. For example, the counter with name "usage" for the "cpu" group of performance counters.
        
    
    .. py:attribute:: perDeviceLevel
    
        Minimum level at which the per device metrics of this type will be collected by vCenter Server. The value for this property for any performance counter is a number from 1 to 4. By default all per device metrics are calculated at level 3 or more. If a certain per device counter is collected at a certain level, the aggregate metric is also calculated at that level, i.e., perDeviceLevel is greater than or equal to level.
        
    
    .. py:attribute:: rollupType
    
        The counter type. Valid values include average, maximum, minimum, latest, summation, or none. This determines the type of statistical values that are returned for the counter. None means that the counter is never rolled up.
        
    
    .. py:attribute:: statsType
    
        Statistics type for the counter. Valid values include absolute, delta, or rate.
        
    
    .. py:attribute:: unitInfo
    
        The unit for the values of the performance counter with its label and summary details. See PerformanceManagerUnit for a description of the valid values.
        
    