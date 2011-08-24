
================================================================================
AlarmTriggeringActionTransitionSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.alarm_triggering_action.AlarmTriggeringAction`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.alarm_triggering_action_transition_spec.AlarmTriggeringActionTransitionSpec
    
    .. py:attribute:: finalState
    
        The state to which the alarm must transition for the action to fire. Valid choices are red, yellow, and green.
        
    
    .. py:attribute:: repeats
    
        Whether or not the action repeats, as per the actionFrequency defined in the enclosing Alarm.
        
    
    .. py:attribute:: startState
    
        The state from which the alarm must transition for the action to fire. Valid choices are red, yellow and green.
        
    