
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ArrayUpdateSpec(DynamicData):
    '''An ArrayUpdateSpec data object type is a common superclass for supporting
        incremental updates to arrays.The common code pattern is:The
        ArrayUpdateSpec contains the following:* : the type of operation being
        performed. * : In the case of a remove operation, the key value that
        identifies the array to be removed.
    '''
    
    def __init__(self, operation, removeKey):
        # MUST define these
        super(ArrayUpdateSpec, self).__init__()
    
        self.data['operation'] = operation
        self.data['removeKey'] = removeKey
    
    
    @property
    def operation(self):
        '''The type of operation being performed on the specified virtual device.
        '''
        return self.data['operation']

    @property
    def removeKey(self):
        '''Key for the element to be removed. Only used if the operation is "remove".
        '''
        return self.data['removeKey']

