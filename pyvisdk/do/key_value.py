
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class KeyValue(DynamicData):
    '''Non-localized key/value pair
    '''
    
    def __init__(self, key, value):
        # MUST define these
        super(KeyValue, self).__init__()
    
        self.data['key'] = key
        self.data['value'] = value
    
    
    @property
    def key(self):
        '''Key.
        '''
        return self.data['key']

    @property
    def value(self):
        '''Value.
        '''
        return self.data['value']

