
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventManager(BaseEntity):
    '''This managed object type provides properties and methods for event management
        support. Event objects are used to record significant state changes of
        managed entities.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.EventManager):
        # MUST define these
        super(EventManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def maxCollector(self):
        '''
        For each client, the maximum number of event collectors that can exist
        simultaneously.
        '''
        return self.update('maxCollector')


    def CreateCollectorForEvents(self, filter):
        '''Creates an event history collector, which is a specialized history collector that
        provides Event objects.Event collectors do not persist beyond the current
        client session.

        :param filter: The event query filter.


        :rtype: ManagedObjectReference to a EventHistoryCollector 

        '''
        
        return self.delegate("CreateCollectorForEvents")(filter)
        

    def PostEvent(self, eventToPost):
        '''Posts the specified event, optionally associating it with a Task.

        :param eventToPost: Fully-specified event to post

        '''
        
        return self.delegate("PostEvent")(eventToPost)
        

    def QueryEvents(self, filter):
        '''Returns the events in specified filter. Returns empty array when there are not any
        events qualified.

        :param filter: The events qualified.


        :rtype: Event[] 

        '''
        
        return self.delegate("QueryEvents")(filter)
        

    def RetrieveArgumentDescription(self, eventTypeId):
        '''Retrieves the argument meta-data for a given Event type

        :param eventTypeId: 


        :rtype: EventArgDesc[] 

        '''
        
        return self.delegate("RetrieveArgumentDescription")(eventTypeId)
        

    def LogUserEvent(self, msg):
        '''Logs a user defined event against a particular managed entity.

        :param msg: The message to be logged.

        '''
        
        return self.delegate("LogUserEvent")(msg)
        
