
from pyvisdk.do.inheritable_policy import InheritablePolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class BoolPolicy(InheritablePolicy):
    '''The boolean type of setting or configuration that may get an inherited value.
    '''
    
    def __init__(self, value):
        # MUST define these
        super(BoolPolicy, self).__init__()
    
        self.data['value'] = value
    
    
    @property
    def value(self):
        '''The boolean value that is either set or inherited.
        '''
        return self.data['value']

