
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCpuPowerManagementInfo(DynamicData):
    '''The CpuPowerManagementInfo data object type describes supported power management
        and current policy.
    '''
    
    def __init__(self, currentPolicy, hardwareSupport):
        # MUST define these
        super(HostCpuPowerManagementInfo, self).__init__()
    
        self.data['currentPolicy'] = currentPolicy
        self.data['hardwareSupport'] = hardwareSupport
    
    
    @property
    def currentPolicy(self):
        '''Information about current CPU power management policy.
        '''
        return self.data['currentPolicy']

    @property
    def hardwareSupport(self):
        '''Information about supported CPU power management.
        '''
        return self.data['hardwareSupport']

