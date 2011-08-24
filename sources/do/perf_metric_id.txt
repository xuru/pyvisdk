
================================================================================
PerfMetricId
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.metric_alarm_expression.MetricAlarmExpression`,
    :py:class:`~pyvisdk.do.perf_metric_series.PerfMetricSeries`,
    :py:class:`~pyvisdk.do.perf_query_spec.PerfQuerySpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_available_perf_metric.QueryAvailablePerfMetric`
    
.. class:: pyvisdk.do.perf_metric_id.PerfMetricId
    
    .. py:attribute:: counterId
    
        The ID of the counter for the metric.
        
    
    .. py:attribute:: instance
    
        An identifier that is derived from configuration names for the device associated with the metric. It identifies the instance of the metric with its source. This property may be empty. * For memory and aggregated statistics, this property is empty. * For host and virtual machine devices, this property contains the name of the device, such as the name of the host-bus adapter or the name of the virtual Ethernet adapter. For example, mpx.vmhba33:C0:T0:L0 or vmnic0: * For a CPU, this property identifies the numeric position within the CPU core, such as 0, 1, 2, 3. * For a virtual disk, this property identifies the file type: * DISKFILE, for virtual machine base-disk files * SWAPFILE, for virtual machine swap files * DELTAFILE, for virtual machine snapshot overhead files * OTHERFILE, for all other files of a virtual machine
        
    