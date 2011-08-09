
from pyvisdk.do.option_type import OptionType
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ChoiceOption(OptionType):
    '''The ChoiceOption data object type defines a set of supported string values, a
        localizable description for each value, and the default value.
    '''
    
    def __init__(self, choiceInfo, defaultIndex):
        # MUST define these
        super(ChoiceOption, self).__init__()
    
        self.data['choiceInfo'] = choiceInfo
        self.data['defaultIndex'] = defaultIndex
    
    
    @property
    def choiceInfo(self):
        '''The set of possible selections and descriptions.
        '''
        return self.data['choiceInfo']

    @property
    def defaultIndex(self):
        '''The index in ChoiceOption.value that serves as the default value.
        '''
        return self.data['defaultIndex']

