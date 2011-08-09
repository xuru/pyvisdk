
from pyvisdk.do.customization_identity_settings import CustomizationIdentitySettings
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationSysprepText(CustomizationIdentitySettings):
    '''An alternate way to specify the answer file. This string is more or less written
        exactly to the answer file on the target virtual disk.
    '''
    
    def __init__(self, value):
        # MUST define these
        super(CustomizationSysprepText, self).__init__()
    
        self.data['value'] = value
    
    
    @property
    def value(self):
        '''Text for the
        '''
        return self.data['value']

