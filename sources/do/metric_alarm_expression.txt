
================================================================================
MetricAlarmExpression
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.metric_alarm_operator.MetricAlarmOperator`,
    :py:class:`~pyvisdk.do.perf_metric_id.PerfMetricId`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.alarm_expression.AlarmExpression`
    
.. class:: pyvisdk.do.metric_alarm_expression.MetricAlarmExpression
    
    .. py:attribute:: metric
    
        The instance of the metric.
        
    
    .. py:attribute:: operator
    
        The operation to be tested on the metric.
        
    
    .. py:attribute:: red
    
        Whether or not to test for a red condition. If not set, do not calculate red status. If set, it contains the threshold value that triggers red status.
        
    
    .. py:attribute:: redInterval
    
        Time interval in seconds for which the red condition must be true before the red status is triggered. If unset, the red status is triggered immediately when the red condition becomes true.
        
    
    .. py:attribute:: type
    
        Name of the object type containing the property.
        
    
    .. py:attribute:: yellow
    
        Whether or not to test for a yellow condition. If not set, do not calculate yellow status. If set, it contains the threshold value that triggers yellow status.
        
    
    .. py:attribute:: yellowInterval
    
        Time interval in seconds for which the yellow condition must be true before the yellow status is triggered. If unset, the yellow status is triggered immediately when the yellow condition becomes true.
        
    