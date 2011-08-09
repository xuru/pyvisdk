
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerformanceStatisticsDescription(DynamicData):
    '''Data object to capture all information needed to describe a sample inventory.
    '''
    
    def __init__(self, intervals):
        # MUST define these
        super(PerformanceStatisticsDescription, self).__init__()
    
        self.data['intervals'] = intervals
    
    
    @property
    def intervals(self):
        '''Historic interval setting. Default value is the same as the historic interval
        settings of the current instance of running VC.
        '''
        return self.data['intervals']

