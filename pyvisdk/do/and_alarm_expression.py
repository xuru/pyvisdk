
from pyvisdk.do.alarm_expression import AlarmExpression
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AndAlarmExpression(AlarmExpression):
    '''A data object type that links multiple alarm expressions with AND operators.
    '''
    
    def __init__(self, expression):
        # MUST define these
        super(AndAlarmExpression, self).__init__()
    
        self.data['expression'] = expression
    
    
    @property
    def expression(self):
        '''List of alarm expressions that define the overall status of the alarm. * The state
        of the alarm expression is gray if all subexpressions are gray. Otherwise,
        gray subexpressions are ignored. * The state is red if all subexpressions
        are red. * Otherwise, the state is yellow if all subexpressions are red or
        yellow. * Otherwise, the state of the alarm expression is green.
        '''
        return self.data['expression']

