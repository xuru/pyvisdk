
================================================================================
EventFilterSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_collector_for_events.CreateCollectorForEvents`,
    :py:meth:`~pyvisdk.do.query_events.QueryEvents`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.alarm.Alarm`,
    :py:class:`~pyvisdk.do.event_filter_spec_by_entity.EventFilterSpecByEntity`,
    :py:class:`~pyvisdk.do.event_filter_spec_by_time.EventFilterSpecByTime`,
    :py:class:`~pyvisdk.do.event_filter_spec_by_username.EventFilterSpecByUsername`,
    :py:class:`~pyvisdk.do.scheduled_task.ScheduledTask`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.event_filter_spec.EventFilterSpec
    
    .. py:attribute:: alarm
    
        This property, if set, limits the set of collected events to those associated with the specified alarm. If the property is not set, events are collected regardless of their association with alarms.
        
    
    .. py:attribute:: category
    
        This property, if set, limits the set of collected events to those associated with the specified category. If the property is not set, events are collected regardless of their association with any category. "category" here is the same as Event.severity.
        
    
    .. py:attribute:: disableFullMessage
    
        Flag to specify whether or not to prepare the full formatted message for each event. If the property is not set, the collected events do not include the full formatted message.
        
    
    .. py:attribute:: entity
    
        The filter specification for retrieving events by managed entity. If the property is not set, then events attached to all managed entities are collected.
        
    
    .. py:attribute:: eventChainId
    
        The filter specification for retrieving events by chain ID. If the property is not set, events with any chain ID are collected.
        
    
    .. py:attribute:: eventTypeId
    
        This property, if set, limits the set of collected events to those specified types.
        
    
    .. py:attribute:: scheduledTask
    
        This property, if set, limits the set of collected events to those associated with the specified scheduled task. If the property is not set, events are collected regardless of their association with any scheduled task.
        
    
    .. py:attribute:: tag
    
        This property, if set, limits the set of filtered events to those that have it. If not set, or the size of it 0, the tag of an event is disregarded. A blank string indicates events without tags.
        
    
    .. py:attribute:: time
    
        The filter specification for retrieving tasks by time. If the property is not set, then events with any time stamp are collected.
        
    
    .. py:attribute:: type
    
        This property, if set, limits the set of collected events to those specified types. If the property is not set, events are collected regardless of their types.
        
    
    .. py:attribute:: userName
    
        The filter specification for retrieving events by username. If the property is not set, then events belonging to any user are collected.
        
    