
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventAlarmExpressionComparison(DynamicData):
    '''Encapsulates Comparison of an event's attribute to a value.
    '''
    
    def __init__(self, attributeName, operator, value):
        # MUST define these
        super(EventAlarmExpressionComparison, self).__init__()
    
        self.data['attributeName'] = attributeName
        self.data['operator'] = operator
        self.data['value'] = value
    
    
    @property
    def attributeName(self):
        '''The attribute of the event to compare
        '''
        return self.data['attributeName']

    @property
    def operator(self):
        '''An operator from the list above
        '''
        return self.data['operator']

    @property
    def value(self):
        '''The value to compare against
        '''
        return self.data['value']

