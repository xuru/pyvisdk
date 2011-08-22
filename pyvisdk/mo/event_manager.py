
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
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
    
    
    
    def CreateCollectorForEvents(self):
        '''Creates an event history collector, which is a specialized history collector
        that provides Event objects.Event collectors do not persist beyond the current
        client session.
        :rtype: ManagedObjectReference to a EventHistoryCollector
        :returns: 
        '''
        return self.delegate("CreateCollectorForEvents")()
    
    def LogUserEvent(self):
        '''Logs a user defined event against a particular managed entity.
        :rtype: None
        :returns: 
        '''
        return self.delegate("LogUserEvent")()
    
    def PostEvent(self):
        '''Posts the specified event, optionally associating it with a Task.
        :rtype: None
        :returns: 
        '''
        return self.delegate("PostEvent")()
    
    def QueryEvents(self):
        '''Returns the events in specified filter. Returns empty array when there are not
        any events qualified.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryEvents")()
    
    def RetrieveArgumentDescription(self):
        '''Retrieves the argument meta-data for a given Event type
        :rtype: 
        :returns: 
        '''
        return self.delegate("RetrieveArgumentDescription")()