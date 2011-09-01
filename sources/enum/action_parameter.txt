
==================================================================================================
ActionParameter
==================================================================================================

.. describe:: ActionParameter

    These constant strings can be used as parameters in user-specified email subject and body templates as well as in scripts. The action processor in VirtualCenter substitutes the run-time values for the parameters. For example, an email subject provided by the client could be the string: . Or a script action provided could be:
    
    
    .. py:data:: ActionParameter.alarm
    
        The object of the triggering alarm.
        
    
    .. py:data:: ActionParameter.alarmName
    
        The name of the triggering alarm.
        
    
    .. py:data:: ActionParameter.declaringSummary
    
        A summary of declarations made during the triggering of the alarm.
        
    
    .. py:data:: ActionParameter.eventDescription
    
        The event description.
        
    
    .. py:data:: ActionParameter.newStatus
    
        The status after the alarm is triggered.
        
    
    .. py:data:: ActionParameter.oldStatus
    
        The status prior to the alarm being triggered.
        
    
    .. py:data:: ActionParameter.target
    
        The object of the entity where the alarm is assocaited.
        
    
    .. py:data:: ActionParameter.targetName
    
        The name of the entity where the alarm is triggered.
        
    
    .. py:data:: ActionParameter.triggeringSummary
    
        A summary of information involved in triggering the alarm.
        
    