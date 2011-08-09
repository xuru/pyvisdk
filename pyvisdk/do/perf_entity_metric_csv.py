
from pyvisdk.do.perf_entity_metric_base import PerfEntityMetricBase
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfEntityMetricCSV(PerfEntityMetricBase):
    '''This data object type stores metric values for a specific entity in CSV format.
    '''
    
    def __init__(self, sampleInfoCSV, value):
        # MUST define these
        super(PerfEntityMetricCSV, self).__init__()
    
        self.data['sampleInfoCSV'] = sampleInfoCSV
        self.data['value'] = value
    
    
    @property
    def sampleInfoCSV(self):
        '''The PerfSampleInfo encoded in the following CSV format: [interval1], [date1],
        [interval2], [date2], and so on.
        '''
        return self.data['sampleInfoCSV']

    @property
    def value(self):
        '''Metric values corresponding to the samples collected in this list.
        '''
        return self.data['value']

