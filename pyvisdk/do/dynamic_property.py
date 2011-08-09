
from pyvisdk.base.base_data import BaseData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DynamicProperty(BaseData):
    '''The DynamicProperty data object type represents a name-value pair.
    '''
    
    def __init__(self, name, val):
        # MUST define these
        super(DynamicProperty, self).__init__()
    
        self.data['name'] = name
        self.data['val'] = val
    
    
    @property
    def name(self):
        '''Path to the property.
        '''
        return self.data['name']

    @property
    def val(self):
        '''Value of the property.
        '''
        return self.data['val']

