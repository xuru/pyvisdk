
from pyvisdk.do.perf_entity_metric_base import PerfEntityMetricBase
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfEntityMetric(PerfEntityMetricBase):
    '''This data object type stores values and metadata for metrics associated with a
        specific entity, in 'normal' format.
    '''
    
    def __init__(self, sampleInfo, value):
        # MUST define these
        super(PerfEntityMetric, self).__init__()
    
        self.data['sampleInfo'] = sampleInfo
        self.data['value'] = value
    
    
    @property
    def sampleInfo(self):
        '''A list of objects containing information (an interval and a timestamp) about the
        samples collected.
        '''
        return self.data['sampleInfo']

    @property
    def value(self):
        '''A list of values that corresponds to the samples collected.
        '''
        return self.data['value']

