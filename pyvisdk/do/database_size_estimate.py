
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatabaseSizeEstimate(DynamicData):
    '''DatabaseSizeEstimate contains information about the size required to by the
        database.
    '''
    
    def __init__(self, size):
        # MUST define these
        super(DatabaseSizeEstimate, self).__init__()
    
        self.data['size'] = size
    
    
    @property
    def size(self):
        '''The estimated size required in MB
        '''
        return self.data['size']

