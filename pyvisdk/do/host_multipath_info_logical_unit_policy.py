
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMultipathInfoLogicalUnitPolicy(DynamicData):
    '''This data object type describes a path selection policy for for a device. This
        policy determines how paths should be utilized when accessing a device.
    '''
    
    def __init__(self, policy):
        # MUST define these
        super(HostMultipathInfoLogicalUnitPolicy, self).__init__()
    
        self.data['policy'] = policy
    
    
    @property
    def policy(self):
        '''The string representing the multipath policy. Valid strings include: *
        '''
        return self.data['policy']

