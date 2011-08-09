
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MethodActionArgument(DynamicData):
    '''This data object type defines a named argument for an operation.
    '''
    
    def __init__(self, value):
        # MUST define these
        super(MethodActionArgument, self).__init__()
    
        self.data['value'] = value
    
    
    @property
    def value(self):
        '''The value of the argument.
        '''
        return self.data['value']

