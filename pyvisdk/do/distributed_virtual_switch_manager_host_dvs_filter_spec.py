
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchManagerHostDvsFilterSpec(DynamicData):
    '''Base class for filters to check host compatibility.
    '''
    
    def __init__(self, inclusive):
        # MUST define these
        super(DistributedVirtualSwitchManagerHostDvsFilterSpec, self).__init__()
    
        self.data['inclusive'] = inclusive
    
    
    @property
    def inclusive(self):
        '''If this flag is true, then the filter returns the hosts in the
        DistributedVirtualSwitchManagerHostContainer that satisfy the criteria
        specified by this filter, otherwise it returns hosts that don't meet the
        criteria.
        '''
        return self.data['inclusive']

