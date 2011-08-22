
================================================================================
AlarmTriggeringAction
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.action.Action`,
    :py:class:`~pyvisdk.do.alarm_triggering_action_transition_spec.AlarmTriggeringActionTransitionSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.alarm_action.AlarmAction`
    
.. class:: pyvisdk.do.alarm_triggering_action.AlarmTriggeringAction
    
    .. py:attribute:: action
    
        The action to be done when the alarm is triggered.
        
    
    .. py:attribute:: green2yellow
    
        Flag to specify that the alarm should trigger on a transition from green to yellow.
        
    
    .. py:attribute:: red2yellow
    
        Flag to specify that the alarm should trigger on a transition from red to yellow.
        
    
    .. py:attribute:: transitionSpecs
    
        Indicates on which transitions this action executes and repeats. This is optional only for backwards compatibility.
        
    
    .. py:attribute:: yellow2green
    
        Flag to specify that the alarm should trigger on a transition from yellow to green.
        
    
    .. py:attribute:: yellow2red
    
        Flag to specify that the alarm should trigger on a transition from yellow to red.
        
    