
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PowerSystemCapability(DynamicData):
    '''Power System Capability data object. Exposes policies available in power
        management system.
    '''
    
    def __init__(self, availablePolicy):
        # MUST define these
        super(PowerSystemCapability, self).__init__()
    
        self.data['availablePolicy'] = availablePolicy
    
    
    @property
    def availablePolicy(self):
        '''List of available host power policies.
        '''
        return self.data['availablePolicy']

