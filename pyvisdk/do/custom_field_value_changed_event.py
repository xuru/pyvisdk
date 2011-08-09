
from pyvisdk.do.custom_field_event import CustomFieldEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldValueChangedEvent(CustomFieldEvent):
    '''This event records a change to a custom field value for a particular entity.
    '''
    
    def __init__(self, entity, fieldKey, name, value):
        # MUST define these
        super(CustomFieldValueChangedEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['fieldKey'] = fieldKey
        self.data['name'] = name
        self.data['value'] = value
    
    
    @property
    def entity(self):
        '''The entity on which the field value was changed.
        '''
        return self.data['entity']

    @property
    def fieldKey(self):
        '''The custom field whose value was changed for the entity.
        '''
        return self.data['fieldKey']

    @property
    def name(self):
        '''The name of the custom field at the time the value was changed.
        '''
        return self.data['name']

    @property
    def value(self):
        '''The new value that was set.
        '''
        return self.data['value']

