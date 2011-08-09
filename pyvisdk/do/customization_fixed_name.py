
from pyvisdk.do.customization_name import CustomizationName
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationFixedName(CustomizationName):
    '''A fixed name.
    '''
    
    def __init__(self, name):
        # MUST define these
        super(CustomizationFixedName, self).__init__()
    
        self.data['name'] = name
    
    
    @property
    def name(self):
        '''The virtual machine name specified by the client.
        '''
        return self.data['name']

