
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OptionType(DynamicData):
    '''The base data object type for all options.
    '''
    
    def __init__(self, valueIsReadonly):
        # MUST define these
        super(OptionType, self).__init__()
    
        self.data['valueIsReadonly'] = valueIsReadonly
    
    
    @property
    def valueIsReadonly(self):
        '''The flag to indicate whether or not a user can modify a value belonging to this
        option type. If the flag is not set, the value can be modified.
        '''
        return self.data['valueIsReadonly']

