
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationPassword(DynamicData):
    '''Contains a password string and a flag that specifies whether the string is in
        plain text or encrypted.
    '''
    
    def __init__(self, plainText, value):
        # MUST define these
        super(CustomizationPassword, self).__init__()
    
        self.data['plainText'] = plainText
        self.data['value'] = value
    
    
    @property
    def plainText(self):
        '''Flag to specify whether or not the password is in plain text, rather than
        encrypted.
        '''
        return self.data['plainText']

    @property
    def value(self):
        '''The password string. It is encrypted if the associated plainText flag is false.
        '''
        return self.data['value']

