
from pyvisdk.do.inheritable_policy import InheritablePolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StringPolicy(InheritablePolicy):
    '''The string type of setting or configuration that may get an inherited value.
    '''
    
    def __init__(self, value):
        # MUST define these
        super(StringPolicy, self).__init__()
    
        self.data['value'] = value
    
    
    @property
    def value(self):
        '''The String value that is either set or inherited.
        '''
        return self.data['value']

