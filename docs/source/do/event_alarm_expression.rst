
================================================================================
EventAlarmExpression
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.event_alarm_expression_comparison.EventAlarmExpressionComparison`,
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.alarm_expression.AlarmExpression`
    
.. class:: pyvisdk.do.event_alarm_expression.EventAlarmExpression
    
    .. py:attribute:: comparisons
    
        The attributes/values to compare.
        
    
    .. py:attribute:: eventType
    
        The type of the event to trigger the alarm on.
        
    
    .. py:attribute:: eventTypeId
    
        The eventTypeId of the event to match.
        
    
    .. py:attribute:: objectType
    
        Name of the type of managed object on which the event is logged.
        
    
    .. py:attribute:: status
    
        The alarm's new state when this condition is evaluated and satisfied. If not specified then there is no change to alarm status, and all actions are fired (rather than those for the transition).
        
    