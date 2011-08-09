
from pyvisdk.do.option_type import OptionType
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StringOption(OptionType):
    '''The StringOption data object type is used to define an open-ended string value
        based on an optional subset of valid characters.
    '''
    
    def __init__(self, defaultValue, validCharacters):
        # MUST define these
        super(StringOption, self).__init__()
    
        self.data['defaultValue'] = defaultValue
        self.data['validCharacters'] = validCharacters
    
    
    @property
    def defaultValue(self):
        '''The default value.
        '''
        return self.data['defaultValue']

    @property
    def validCharacters(self):
        '''The string containing the set of valid characters. If a string option is not
        specified, all strings are allowed.
        '''
        return self.data['validCharacters']

