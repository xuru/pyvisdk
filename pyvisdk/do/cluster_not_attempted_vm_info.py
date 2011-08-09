
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterNotAttemptedVmInfo(DynamicData):
    '''This data class reports one virtual machine powerOn failure.
    '''
    
    def __init__(self, fault, vm):
        # MUST define these
        super(ClusterNotAttemptedVmInfo, self).__init__()
    
        self.data['fault'] = fault
        self.data['vm'] = vm
    
    
    @property
    def fault(self):
        '''The exception returned.
        '''
        return self.data['fault']

    @property
    def vm(self):
        '''The virtual machine that can not be powered on.
        '''
        return self.data['vm']

