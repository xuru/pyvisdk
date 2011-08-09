
from pyvisdk.do.custom_field_def_event import CustomFieldDefEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldDefRenamedEvent(CustomFieldDefEvent):
    '''This event records the renaming of a custom field definition.
    '''
    
    def __init__(self, newName):
        # MUST define these
        super(CustomFieldDefRenamedEvent, self).__init__()
    
        self.data['newName'] = newName
    
    
    @property
    def newName(self):
        '''
        '''
        return self.data['newName']

