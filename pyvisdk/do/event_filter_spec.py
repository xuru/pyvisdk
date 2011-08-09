
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventFilterSpec(DynamicData):
    '''Event filter used to query events in the history collector database. The client
        creates an event history collector with a filter specification, then
        retrieves the events from the event history collector.
    '''
    
    def __init__(self, alarm, category, disableFullMessage, entity, eventChainId, eventTypeId, scheduledTask, tag, time, type, userName):
        # MUST define these
        super(EventFilterSpec, self).__init__()
    
        self.data['alarm'] = alarm
        self.data['category'] = category
        self.data['disableFullMessage'] = disableFullMessage
        self.data['entity'] = entity
        self.data['eventChainId'] = eventChainId
        self.data['eventTypeId'] = eventTypeId
        self.data['scheduledTask'] = scheduledTask
        self.data['tag'] = tag
        self.data['time'] = time
        self.data['type'] = type
        self.data['userName'] = userName
    
    
    @property
    def alarm(self):
        '''This property, if set, limits the set of collected events to those associated with
        the specified alarm. If the property is not set, events are collected
        regardless of their association with alarms.
        '''
        return self.data['alarm']

    @property
    def category(self):
        '''This property, if set, limits the set of collected events to those associated with
        the specified category. If the property is not set, events are collected
        regardless of their association with any category. "category" here is the
        same as Event.severity.
        '''
        return self.data['category']

    @property
    def disableFullMessage(self):
        '''Flag to specify whether or not to prepare the full formatted message for each
        event. If the property is not set, the collected events do not include the
        full formatted message.
        '''
        return self.data['disableFullMessage']

    @property
    def entity(self):
        '''The filter specification for retrieving events by managed entity. If the property
        is not set, then events attached to all managed entities are collected.
        '''
        return self.data['entity']

    @property
    def eventChainId(self):
        '''The filter specification for retrieving events by chain ID. If the property is not
        set, events with any chain ID are collected.
        '''
        return self.data['eventChainId']

    @property
    def eventTypeId(self):
        '''This property, if set, limits the set of collected events to those specified
        types.
        '''
        return self.data['eventTypeId']

    @property
    def scheduledTask(self):
        '''This property, if set, limits the set of collected events to those associated with
        the specified scheduled task. If the property is not set, events are
        collected regardless of their association with any scheduled task.
        '''
        return self.data['scheduledTask']

    @property
    def tag(self):
        '''This property, if set, limits the set of filtered events to those that have it. If
        not set, or the size of it 0, the tag of an event is disregarded. A blank
        string indicates events without tags.
        '''
        return self.data['tag']

    @property
    def time(self):
        '''The filter specification for retrieving tasks by time. If the property is not set,
        then events with any time stamp are collected.
        '''
        return self.data['time']

    @property
    def type(self):
        '''This property, if set, limits the set of collected events to those specified
        types. If the property is not set, events are collected regardless of
        their types.
        '''
        return self.data['type']

    @property
    def userName(self):
        '''The filter specification for retrieving events by username. If the property is not
        set, then events belonging to any user are collected.
        '''
        return self.data['userName']

