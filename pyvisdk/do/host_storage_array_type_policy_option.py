
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostStorageArrayTypePolicyOption(DynamicData):
    '''Description of options associated with a native multipathing storage array type
        plugin.
    '''
    
    def __init__(self, policy):
        # MUST define these
        super(HostStorageArrayTypePolicyOption, self).__init__()
    
        self.data['policy'] = policy
    
    
    @property
    def policy(self):
        '''Description of the paths selection policy. Use the key as the identifier.
        '''
        return self.data['policy']

