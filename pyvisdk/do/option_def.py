
from pyvisdk.do.element_description import ElementDescription
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OptionDef(ElementDescription):
    '''Describes a user-defined option. The name of each option is identified by the
        "key" property, inherited from the ElementDescription data object type.
        You can indicate the property's position in a hierarchy by using a dot-
        separated notation. The string preceding the first dot is the top of the
        hierarchy. The hierarchy descends to a new sublevel with each dot. For
        example, "Ethernet.NetworkConnection.Bridged".
    '''
    
    def __init__(self, optionType):
        # MUST define these
        super(OptionDef, self).__init__()
    
        self.data['optionType'] = optionType
    
    
    @property
    def optionType(self):
        '''The option type which defines allowed values.
        '''
        return self.data['optionType']

