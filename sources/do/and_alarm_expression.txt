
================================================================================
AndAlarmExpression
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.alarm_expression.AlarmExpression`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.alarm_expression.AlarmExpression`
    
.. class:: pyvisdk.do.and_alarm_expression.AndAlarmExpression
    
    .. py:attribute:: expression
    
        List of alarm expressions that define the overall status of the alarm. * The state of the alarm expression is gray if all subexpressions are gray. Otherwise, gray subexpressions are ignored. * The state is red if all subexpressions are red. * Otherwise, the state is yellow if all subexpressions are red or yellow. * Otherwise, the state of the alarm expression is green.
        
    