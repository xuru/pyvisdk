
================================================================================
AlarmSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_alarm.CreateAlarm`,
    :py:meth:`~pyvisdk.do.reconfigure_alarm.ReconfigureAlarm`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.alarm_info.AlarmInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.alarm_action.AlarmAction`,
    :py:class:`~pyvisdk.do.alarm_expression.AlarmExpression`,
    :py:class:`~pyvisdk.do.alarm_setting.AlarmSetting`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.alarm_spec.AlarmSpec
    
    .. py:attribute:: action
    
        Action to perform when the alarm is triggered.
        
    
    .. py:attribute:: actionFrequency
    
        Frequency in seconds, which specifies how often appropriate actions should repeat when an alarm does not change state.
        
    
    .. py:attribute:: description
    
        Description of the alarm.
        
    
    .. py:attribute:: enabled
    
        Flag to indicate whether or not the alarm is enabled or disabled.
        
    
    .. py:attribute:: expression
    
        Top-level alarm expression that defines trigger conditions.
        
    
    .. py:attribute:: name
    
        Name of the alarm.
        
    
    .. py:attribute:: setting
    
        Tolerance and maximum frequency settings.
        
    