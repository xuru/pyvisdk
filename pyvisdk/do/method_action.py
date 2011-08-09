
from pyvisdk.do.action import Action
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MethodAction(Action):
    '''This data object type defines an operation and its arguments, invoked on a
        particular entity.
    '''
    
    def __init__(self, argument, name):
        # MUST define these
        super(MethodAction, self).__init__()
    
        self.data['argument'] = argument
        self.data['name'] = name
    
    
    @property
    def argument(self):
        '''An array consisting of the arguments for the operation.
        '''
        return self.data['argument']

    @property
    def name(self):
        '''Name of the operation.
        '''
        return self.data['name']

