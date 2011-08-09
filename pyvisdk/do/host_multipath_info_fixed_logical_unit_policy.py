
from pyvisdk.do.host_multipath_info_logical_unit_policy import HostMultipathInfoLogicalUnitPolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMultipathInfoFixedLogicalUnitPolicy(HostMultipathInfoLogicalUnitPolicy):
    '''This data object type describes a multipathing policy for a logical unit which
        uses a preferred path whenever possible.
    '''
    
    def __init__(self, prefer):
        # MUST define these
        super(HostMultipathInfoFixedLogicalUnitPolicy, self).__init__()
    
        self.data['prefer'] = prefer
    
    
    @property
    def prefer(self):
        '''Preferred path used for the
        '''
        return self.data['prefer']

