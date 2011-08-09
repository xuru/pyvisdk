
from pyvisdk.do.perf_metric_series import PerfMetricSeries
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfMetricSeriesCSV(PerfMetricSeries):
    '''This data object type represents a PerfMetricSeries encoded in CSV format.
    '''
    
    def __init__(self, value):
        # MUST define these
        super(PerfMetricSeriesCSV, self).__init__()
    
        self.data['value'] = value
    
    
    @property
    def value(self):
        '''An array of sample values in CSV format
        '''
        return self.data['value']

