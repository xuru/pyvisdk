
from pyvisdk.do.custom_field_value import CustomFieldValue
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldStringValue(CustomFieldValue):
    '''Subtype for string values (currently the only supported type).
    '''
    
    def __init__(self, value):
        # MUST define these
        super(CustomFieldStringValue, self).__init__()
    
        self.data['value'] = value
    
    
    @property
    def value(self):
        '''Value assigned to the custom field.
        '''
        return self.data['value']

