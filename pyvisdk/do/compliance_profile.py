
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComplianceProfile(DynamicData):
    '''DataObject contains the verifications that need to be done to make sure the entity
        is in compliance.
    '''
    
    def __init__(self, expression, rootExpression):
        # MUST define these
        super(ComplianceProfile, self).__init__()
    
        self.data['expression'] = expression
        self.data['rootExpression'] = rootExpression
    
    
    @property
    def expression(self):
        '''List of expressions that make up the ComplianceChecks.
        '''
        return self.data['expression']

    @property
    def rootExpression(self):
        '''Name of the Expression which is the root of the expression tree.
        '''
        return self.data['rootExpression']

