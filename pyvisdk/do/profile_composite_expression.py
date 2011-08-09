
from pyvisdk.do.profile_expression import ProfileExpression
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileCompositeExpression(ProfileExpression):
    '''DataObject to Compose expressions. It is used to group expressions together. They
        are similar to a parentheses in an expression.
    '''
    
    def __init__(self, expressionName, operator):
        # MUST define these
        super(ProfileCompositeExpression, self).__init__()
    
        self.data['expressionName'] = expressionName
        self.data['operator'] = operator
    
    
    @property
    def expressionName(self):
        '''List of expression names that will be used for this composition. The individual
        expressions will return a boolean. The return values of the individual
        expressions will be used to compute the final return value of the
        CompositeExpression. The expressions specified in the list can themselves
        be CompositeExpressions.
        '''
        return self.data['expressionName']

    @property
    def operator(self):
        '''Logical operator to be applied between the expressions in the composite
        expression. e.g: or, and
        '''
        return self.data['operator']

