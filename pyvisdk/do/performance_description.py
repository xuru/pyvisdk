
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerformanceDescription(DynamicData):
    '''Static strings for performance metrics.
    '''
    
    def __init__(self, counterType, statsType):
        # MUST define these
        super(PerformanceDescription, self).__init__()
    
        self.data['counterType'] = counterType
        self.data['statsType'] = statsType
    
    
    @property
    def counterType(self):
        '''Identifies the type of the counter.
        '''
        return self.data['counterType']

    @property
    def statsType(self):
        '''Identifies the type of statistic.
        '''
        return self.data['statsType']

