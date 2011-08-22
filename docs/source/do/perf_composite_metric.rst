
================================================================================
PerfCompositeMetric
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.perf_entity_metric_base.PerfEntityMetricBase`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_perf_composite.QueryPerfComposite`
    
.. class:: pyvisdk.do.perf_composite_metric.PerfCompositeMetric
    
    .. py:attribute:: childEntity
    
        A list of metrics of performance providers that comprise the aggregated entity. For example, Host is an aggregated entity for virtual machines and virtual machine Folders. ResourcePools are aggregate entities for virtual machines. Host, Folder, and Cluster are aggregate entities for hosts in the cluster or folder.
        
    
    .. py:attribute:: entity
    
        The aggregated entity performance metrics. If it exists, the PerfSampleInfo list of the aggregate entity is a complete list of PerfSampleInfo that could be contained in PerfSampleInfo lists of child entities.
        
    