
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventManager(BaseEntity):
    '''This managed object type provides properties and methods for event management
    support. Event objects are used to record significant state changes of managed
    entities.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.EventManager):
        super(EventManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def description(self):
        '''Static descriptive strings used in events.'''
        return self.update('description')
    @property
    def latestEvent(self):
        '''The latest event that happened on the VirtualCenter server.'''
        return self.update('latestEvent')
    @property
    def maxCollector(self):
        '''For each client, the maximum number of event collectors that can exist
        simultaneously.'''
        return self.update('maxCollector')

    
    
    def CreateCollectorForEvents(self, filter):
        '''Creates an event history collector, which is a specialized history collector
        that provides Event objects.Creates an event history collector, which is a
        specialized history collector that provides Event objects.
        
        :param filter: The event query filter.
        
        '''
        return self.delegate("CreateCollectorForEvents")(filter)
    
    def LogUserEvent(self, entity, msg):
        '''Logs a user defined event against a particular managed entity.
        
        :param entity: The entity against which the event is logged. The entity must be the root folder, a DataCenter, a VirtualMachine, a HostSystem, or a ComputeResource.
        
        :param msg: The message to be logged.
        
        '''
        return self.delegate("LogUserEvent")(entity, msg)
    
    def PostEvent(self, eventToPost, taskInfo=None):
        '''Posts the specified event, optionally associating it with a task.Posts the
        specified event, optionally associating it with a task.Posts the specified
        event, optionally associating it with a task.Posts the specified event,
        optionally associating it with a task.
        
        :param eventToPost: Fully-specified event to post
        
        :param taskInfo: optional task associated with the event
        
        '''
        return self.delegate("PostEvent")(eventToPost, taskInfo)
    
    def QueryEvents(self, filter):
        '''Returns the events in specified filter. Returns empty array when there are not
        any events qualified.
        
        :param filter: The events qualified.
        
        '''
        return self.delegate("QueryEvents")(filter)
    
    def RetrieveArgumentDescription(self, eventTypeId):
        '''Retrieves the argument meta-data for a given Event type
        
        :param eventTypeId: 
        
        '''
        return self.delegate("RetrieveArgumentDescription")(eventTypeId)