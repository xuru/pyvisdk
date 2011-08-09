
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMultipathInfoLogicalUnitStorageArrayTypePolicy(DynamicData):
    '''This data object type describes a storage array type policy for for a device. This
        policy determines how device I/O and management is performed.
    '''
    
    def __init__(self, policy):
        # MUST define these
        super(HostMultipathInfoLogicalUnitStorageArrayTypePolicy, self).__init__()
    
        self.data['policy'] = policy
    
    
    @property
    def policy(self):
        '''The string indicates the storage array type policy.
        '''
        return self.data['policy']

