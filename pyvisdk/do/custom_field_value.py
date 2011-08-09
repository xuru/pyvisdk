
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldValue(DynamicData):
    '''Base type for storing values.
    '''
    
    def __init__(self, key):
        # MUST define these
        super(CustomFieldValue, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''The ID of the field to which this value belongs.
        '''
        return self.data['key']

