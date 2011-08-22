
================================================================================
PerfProviderSummary
================================================================================


.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_perf_provider_summary.QueryPerfProviderSummary`
    
.. class:: pyvisdk.do.perf_provider_summary.PerfProviderSummary
    
    .. py:attribute:: currentSupported
    
        True if this entity supports real-time (current) statistics; false if it does not. If this property is true for an entity, a client application can set the intervalId of the PerfQuerySpec (passed to the QueryPerf operation) to the refreshRate to obtain the maximum information possible for the entity.
        
    
    .. py:attribute:: entity
    
        Reference to the performance provider, the managed object that provides real-time or historical metrics. The managed objects include but are not limited to managed entities, such as host systems, virtual machines, and resource pools.
        
    
    .. py:attribute:: refreshRate
    
        Number of seconds between the generation of each counter. This value applies only to entities that support real-time (current) statistics.
        
    
    .. py:attribute:: summarySupported
    
        True if this entity supports historical (aggregated) statistics; false if it does not. When this property is true for an entity, a client application can set the intervalId of QueryPerf to one of the historical intervals to obtain historical statistics for this entity.
        
    