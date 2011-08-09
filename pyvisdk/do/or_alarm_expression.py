
from pyvisdk.do.alarm_expression import AlarmExpression
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OrAlarmExpression(AlarmExpression):
    '''A data object type that links multiple alarm expressions with OR operators.
    '''
    
    def __init__(self, expression):
        # MUST define these
        super(OrAlarmExpression, self).__init__()
    
        self.data['expression'] = expression
    
    
    @property
    def expression(self):
        '''List of alarm expressions that define the overall status of the alarm. * The state
        of the alarm expression is gray if all subexpressions are gray. Otherwise,
        gray subexpressions are ignored. * The state is red if any subexpression
        is red. * Otherwise, the state is yellow if any subexpression is yellow. *
        Otherwise, the state of the alarm expression is green.
        '''
        return self.data['expression']

