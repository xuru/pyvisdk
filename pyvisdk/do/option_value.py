
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OptionValue(DynamicData):
    '''Describes the key/value pair of a configured option.
    '''
    
    def __init__(self, key, value):
        # MUST define these
        super(OptionValue, self).__init__()
    
        self.data['key'] = key
        self.data['value'] = value
    
    
    @property
    def key(self):
        '''The name of the option using dot notation to reflect the option's position in a
        hierarchy. For example, you might have an option called "Ethernet" and
        another option that is a child of that called "Connection". In this case,
        the key for the latter could be defined as "Ethernet.Connection"
        '''
        return self.data['key']

    @property
    def value(self):
        '''The value of the option. The Any data object type enables you to define any value
        for the option. Typically, however, the value of an option is of type
        String or Integer.
        '''
        return self.data['value']

