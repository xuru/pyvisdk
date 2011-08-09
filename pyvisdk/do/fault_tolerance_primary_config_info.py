
from pyvisdk.do.fault_tolerance_config_info import FaultToleranceConfigInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FaultTolerancePrimaryConfigInfo(FaultToleranceConfigInfo):
    '''FaultTolerancePrimaryConfigInfo is a data object type containing Fault Tolerance
        settings for a primary virtual machine in a fault tolerance group
    '''
    
    def __init__(self, secondaries):
        # MUST define these
        super(FaultTolerancePrimaryConfigInfo, self).__init__()
    
        self.data['secondaries'] = secondaries
    
    
    @property
    def secondaries(self):
        '''
        '''
        return self.data['secondaries']

