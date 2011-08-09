
from pyvisdk.do.profile_expression import ProfileExpression
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileSimpleExpression(ProfileExpression):
    '''DataObject represents a pre-defined expression
    '''
    
    def __init__(self, expressionType, parameter):
        # MUST define these
        super(ProfileSimpleExpression, self).__init__()
    
        self.data['expressionType'] = expressionType
        self.data['parameter'] = parameter
    
    
    @property
    def expressionType(self):
        '''Type of the simple expression to instantiate. The expressionType should be derived
        from the available expressions as listed in the metadata.
        '''
        return self.data['expressionType']

    @property
    def parameter(self):
        '''The parameters for the expressionType. The list of parameters needed for a simple
        expression can be obtained from the metadata.
        '''
        return self.data['parameter']

