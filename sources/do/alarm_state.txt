
================================================================================
AlarmState
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.alarm.Alarm`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`,
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.get_alarm_state.GetAlarmState`
    
.. class:: pyvisdk.do.alarm_state.AlarmState
    
    .. py:attribute:: acknowledged
    
        Flag to indicate if the alarm's actions have been acknowledged for the associated ManagedEntity.
        
    
    .. py:attribute:: acknowledgedByUser
    
        The user who acknowledged this triggering. If the triggering has not been acknowledged, then the value is not valid.
        
    
    .. py:attribute:: acknowledgedTime
    
        The time this triggering was acknowledged. If the triggering has not been acknowledged, then the value is not valid.
        
    
    .. py:attribute:: alarm
    
        Alarm object from which the AlarmState object is instantiated.
        
    
    .. py:attribute:: entity
    
        Entity on which the alarm is instantiated.
        
    
    .. py:attribute:: key
    
        Unique key that identifies the alarm.
        
    
    .. py:attribute:: overallStatus
    
        Overall status of the alarm object. This is the value of the alarm's top-level expression.
        
    
    .. py:attribute:: time
    
        Time the alarm triggered.
        
    