
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostStorageOperationalInfo(DynamicData):
    '''Data class describing operational information of a storage element
    '''
    
    def __init__(self, property, value):
        # MUST define these
        super(HostStorageOperationalInfo, self).__init__()
    
        self.data['property'] = property
        self.data['value'] = value
    
    
    @property
    def property_(self):
        '''The property of interest for the storage element
        '''
        return self.data['property']

    @property
    def value(self):
        '''The property value for the storage element
        '''
        return self.data['value']

