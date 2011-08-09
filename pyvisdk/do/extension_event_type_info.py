
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensionEventTypeInfo(DynamicData):
    '''This data object type describes event types defined by the extension.
    '''
    
    def __init__(self, eventID, eventTypeSchema):
        # MUST define these
        super(ExtensionEventTypeInfo, self).__init__()
    
        self.data['eventID'] = eventID
        self.data['eventTypeSchema'] = eventTypeSchema
    
    
    @property
    def eventID(self):
        '''The ID of the event type. Should follow java package naming conventions for
        uniqueness.
        '''
        return self.data['eventID']

    @property
    def eventTypeSchema(self):
        '''Optional XML descriptor for the EventType. The structure of this descriptor is:
        '''
        return self.data['eventTypeSchema']

