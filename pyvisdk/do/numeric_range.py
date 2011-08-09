
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NumericRange(DynamicData):
    '''The class that describe an integer range.
    '''
    
    def __init__(self, end, start):
        # MUST define these
        super(NumericRange, self).__init__()
    
        self.data['end'] = end
        self.data['start'] = start
    
    
    @property
    def end(self):
        '''The ending number (inclusive).
        '''
        return self.data['end']

    @property
    def start(self):
        '''The starting number.
        '''
        return self.data['start']

