
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HealthSystemRuntime(DynamicData):
    '''The system health runtime information
    '''
    
    def __init__(self, hardwareStatusInfo, systemHealthInfo):
        # MUST define these
        super(HealthSystemRuntime, self).__init__()
    
        self.data['hardwareStatusInfo'] = hardwareStatusInfo
        self.data['systemHealthInfo'] = systemHealthInfo
    
    
    @property
    def hardwareStatusInfo(self):
        '''Available hardware health information
        '''
        return self.data['hardwareStatusInfo']

    @property
    def systemHealthInfo(self):
        '''Available system health information
        '''
        return self.data['systemHealthInfo']

