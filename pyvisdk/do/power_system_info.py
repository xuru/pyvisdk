
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PowerSystemInfo(DynamicData):
    '''Power System Info data object. Shows current state of power management system.
    '''
    
    def __init__(self, currentPolicy):
        # MUST define these
        super(PowerSystemInfo, self).__init__()
    
        self.data['currentPolicy'] = currentPolicy
    
    
    @property
    def currentPolicy(self):
        '''Currently selected host power management policy. This property can have one of the
        values from availablePolicy.
        '''
        return self.data['currentPolicy']

