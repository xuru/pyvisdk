
from pyvisdk.do.option_type import OptionType
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class BoolOption(OptionType):
    '''The BoolOption data object type describes if an option is supported ("true") and
        if the option is set to "true" or "false" by default.
    '''
    
    def __init__(self, defaultValue, supported):
        # MUST define these
        super(BoolOption, self).__init__()
    
        self.data['defaultValue'] = defaultValue
        self.data['supported'] = supported
    
    
    @property
    def defaultValue(self):
        '''The default value for the option.
        '''
        return self.data['defaultValue']

    @property
    def supported(self):
        '''The flag to indicate whether or not the option is supported.
        '''
        return self.data['supported']

