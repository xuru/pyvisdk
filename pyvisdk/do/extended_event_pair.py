
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtendedEventPair(DynamicData):
    '''key/value pair
    '''
    
    def __init__(self, key, value):
        # MUST define these
        super(ExtendedEventPair, self).__init__()
    
        self.data['key'] = key
        self.data['value'] = value
    
    
    @property
    def key(self):
        '''
        '''
        return self.data['key']

    @property
    def value(self):
        '''
        '''
        return self.data['value']

