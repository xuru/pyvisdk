
================================================================================
StateAlarmExpression
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.state_alarm_operator.StateAlarmOperator`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.alarm_expression.AlarmExpression`
    
.. class:: pyvisdk.do.state_alarm_expression.StateAlarmExpression
    
    .. py:attribute:: operator
    
        The operation to be tested on the target state.
        
    
    .. py:attribute:: red
    
        Whether or not to test for a red condition. If this property is not set, do not calculate red status.
        
    
    .. py:attribute:: statePath
    
        Path of the state property.
        
    
    .. py:attribute:: type
    
        Name of the object type containing the property.
        
    
    .. py:attribute:: yellow
    
        Whether or not to test for a yellow condition. If this property is not set, do not calculate yellow status.
        
    