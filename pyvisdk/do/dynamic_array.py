
from pyvisdk.base.base_data import BaseData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DynamicArray(BaseData):
    '''DynamicArray is a data object type that represents an array of dynamically-typed
        objects. A client should only see a DynamicArray object when the element
        type is unknown (meaning the type is newer than the client). Otherwise, a
        client would see the type as T[] where T is known.
    '''
    
    def __init__(self, dynamicType, val):
        # MUST define these
        super(DynamicArray, self).__init__()
    
        self.data['dynamicType'] = dynamicType
        self.data['val'] = val
    
    
    @property
    def dynamicType(self):
        '''Reserved.
        '''
        return self.data['dynamicType']

    @property
    def val(self):
        '''Array of dynamic values.
        '''
        return self.data['val']

