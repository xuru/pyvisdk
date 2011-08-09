
from pyvisdk.do.fault_tolerance_config_info import FaultToleranceConfigInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FaultToleranceSecondaryConfigInfo(FaultToleranceConfigInfo):
    '''FaultToleranceSecondaryConfigInfo is a data object type containing Fault Tolerance
        settings for a secondary virtual machine in a fault tolerance group
    '''
    
    def __init__(self, primaryVM):
        # MUST define these
        super(FaultToleranceSecondaryConfigInfo, self).__init__()
    
        self.data['primaryVM'] = primaryVM
    
    
    @property
    def primaryVM(self):
        '''
        '''
        return self.data['primaryVM']

