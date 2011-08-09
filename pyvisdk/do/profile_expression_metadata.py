
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileExpressionMetadata(DynamicData):
    '''DataObject to represent the metadata associated with a SimpleExpression.
    '''
    
    def __init__(self, expressionId, parameter):
        # MUST define these
        super(ProfileExpressionMetadata, self).__init__()
    
        self.data['expressionId'] = expressionId
        self.data['parameter'] = parameter
    
    
    @property
    def expressionId(self):
        '''Id of the SimpleExpression
        '''
        return self.data['expressionId']

    @property
    def parameter(self):
        '''Parameters that can be specified for this SimpleExpression
        '''
        return self.data['parameter']

