
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PasswordField(DynamicData):
    '''DataObject which represents a Password field. Password is functionally equivalent
        to String.
    '''
    
    def __init__(self, value):
        # MUST define these
        super(PasswordField, self).__init__()
    
        self.data['value'] = value
    
    
    @property
    def value(self):
        '''
        '''
        return self.data['value']

