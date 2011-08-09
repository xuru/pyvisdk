
from pyvisdk.do.general_event import GeneralEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtendedEvent(GeneralEvent):
    '''This event is the base class for extended events.
    '''
    
    def __init__(self, data, eventTypeId, managedObject):
        # MUST define these
        super(ExtendedEvent, self).__init__()
    
        self.data['data'] = data
        self.data['eventTypeId'] = eventTypeId
        self.data['managedObject'] = managedObject
    
    
    @property
    def data(self):
        '''Key/value pairs associated with event.
        '''
        return self.data['data']

    @property
    def eventTypeId(self):
        '''The id of the type of extended event.
        '''
        return self.data['eventTypeId']

    @property
    def managedObject(self):
        '''The object on which the event was logged.
        '''
        return self.data['managedObject']

