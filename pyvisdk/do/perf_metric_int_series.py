
from pyvisdk.do.perf_metric_series import PerfMetricSeries
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfMetricIntSeries(PerfMetricSeries):
    '''This data object type describes integer metric values. The size of the array must
        match the size of sampleInfo property in the PerfEntityMetric that
        contains this series.
    '''
    
    def __init__(self, value):
        # MUST define these
        super(PerfMetricIntSeries, self).__init__()
    
        self.data['value'] = value
    
    
    @property
    def value(self):
        '''An array of 64-bit integer values. The size of the array matches the size as the
        PerfSampleInfo, because the values can only be interpreted in the context
        of the sample that generated the value.
        '''
        return self.data['value']

