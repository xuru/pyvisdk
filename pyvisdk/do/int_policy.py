
from pyvisdk.do.inheritable_policy import InheritablePolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class IntPolicy(InheritablePolicy):
    '''The integer type of setting or configuration that may get an inherited value.
    '''
    
    def __init__(self, value):
        # MUST define these
        super(IntPolicy, self).__init__()
    
        self.data['value'] = value
    
    
    @property
    def value(self):
        '''The integer value that is either set or inherited.
        '''
        return self.data['value']

