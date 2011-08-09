
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchManagerCompatibilityResult(DynamicData):
    '''This is the return type for the checkCompatibility method. This object has a host
        property and optionally a fault which would be populated only if that host
        is not compatible with a given dvsProductSpec. If the host is compatible
        then the error property would be unset.
    '''
    
    def __init__(self, error, host):
        # MUST define these
        super(DistributedVirtualSwitchManagerCompatibilityResult, self).__init__()
    
        self.data['error'] = error
        self.data['host'] = host
    
    
    @property
    def error(self):
        '''This property contains the faults that makes the host not compatible with a given
        DvsProductSpec. For example, a host might not be compatible because it's
        an older version of ESX that doesn't support DVS.
        '''
        return self.data['error']

    @property
    def host(self):
        '''The host for which results are annotated. The whole object will be filtered out if
        the caller did not have view permissions on the host entity.
        '''
        return self.data['host']

