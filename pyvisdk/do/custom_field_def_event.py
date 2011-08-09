
from pyvisdk.do.custom_field_event import CustomFieldEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldDefEvent(CustomFieldEvent):
    '''This event records a custom field definition event.
    '''
    
    def __init__(self, fieldKey, name):
        # MUST define these
        super(CustomFieldDefEvent, self).__init__()
    
        self.data['fieldKey'] = fieldKey
        self.data['name'] = name
    
    
    @property
    def fieldKey(self):
        '''The unique identifier of the custom field definition.
        '''
        return self.data['fieldKey']

    @property
    def name(self):
        '''The name of the custom field.
        '''
        return self.data['name']

