
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfEntityMetricBase(DynamicData):
    '''Base type for the various PerfEntityMetric encodings.
    '''
    
    def __init__(self, entity):
        # MUST define these
        super(PerfEntityMetricBase, self).__init__()
    
        self.data['entity'] = entity
    
    
    @property
    def entity(self):
        '''Performance provider ID.
        '''
        return self.data['entity']

