
================================================================================
OrAlarmExpression
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.alarm_expression.AlarmExpression`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.alarm_expression.AlarmExpression`
    
.. class:: pyvisdk.do.or_alarm_expression.OrAlarmExpression
    
    .. py:attribute:: expression
    
        List of alarm expressions that define the overall status of the alarm. * The state of the alarm expression is gray if all subexpressions are gray. Otherwise, gray subexpressions are ignored. * The state is red if any subexpression is red. * Otherwise, the state is yellow if any subexpression is yellow. * Otherwise, the state of the alarm expression is green.
        
    