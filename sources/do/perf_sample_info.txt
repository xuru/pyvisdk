
================================================================================
PerfSampleInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.perf_entity_metric.PerfEntityMetric`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.perf_sample_info.PerfSampleInfo
    
    .. py:attribute:: interval
    
        The interval in seconds for which performance statistics were collected. This can be the refreshRate of the managed object for which this statistics was collected or one of the intervals for historical statistics configured in the system. See UpdatePerfInterval for more information about the intervals configured in the system.
        
    
    .. py:attribute:: timestamp
    
        The time at which the sample was collected.
        
    