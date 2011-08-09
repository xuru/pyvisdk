
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class KeyAnyValue(DynamicData):
    '''Non-localized key/value pair in which the the value can be of any type.
    '''
    
    def __init__(self, key, value):
        # MUST define these
        super(KeyAnyValue, self).__init__()
    
        self.data['key'] = key
        self.data['value'] = value
    
    
    @property
    def key(self):
        '''the key
        '''
        return self.data['key']

    @property
    def value(self):
        '''the value
        '''
        return self.data['value']

