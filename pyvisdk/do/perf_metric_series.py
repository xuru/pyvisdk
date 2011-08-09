
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfMetricSeries(DynamicData):
    '''This is a generic data object type that stores values for a specific performance
        metric. Useful data objects that store actual metric values extend this
        data object (see PerfMetricIntSeries).
    '''
    
    def __init__(self, id):
        # MUST define these
        super(PerfMetricSeries, self).__init__()
    
        self.data['id'] = id
    
    
    @property
    def id(self):
        '''An identifier for the performance metric.
        '''
        return self.data['id']

