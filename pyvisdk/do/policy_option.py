
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PolicyOption(DynamicData):
    '''This data object represents a policy option.
    '''
    
    def __init__(self, id, parameter):
        # MUST define these
        super(PolicyOption, self).__init__()
    
        self.data['id'] = id
        self.data['parameter'] = parameter
    
    
    @property
    def id(self):
        '''The id of the PolicyOption
        '''
        return self.data['id']

    @property
    def parameter(self):
        '''The parameters to the PolicyOption. Any parameter that is not marked as optional
        in the PolicyOption's metadata needs to be included here.
        '''
        return self.data['parameter']

