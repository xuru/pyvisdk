
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DiskChangeExtent(DynamicData):
    '''An area of the disk flagged as modified
    '''
    
    def __init__(self, length, start):
        # MUST define these
        super(DiskChangeExtent, self).__init__()
    
        self.data['length'] = length
        self.data['start'] = start
    
    
    @property
    def length(self):
        '''Length (in bytes) of modified area
        '''
        return self.data['length']

    @property
    def start(self):
        '''Start offset (in bytes) of modified area
        '''
        return self.data['start']

