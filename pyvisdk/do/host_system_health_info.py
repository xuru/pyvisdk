
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSystemHealthInfo(DynamicData):
    '''This data object provides information about the health of the phyical system. The
        data is retrieved from numeric sensor probes.
    '''
    
    def __init__(self, numericSensorInfo):
        # MUST define these
        super(HostSystemHealthInfo, self).__init__()
    
        self.data['numericSensorInfo'] = numericSensorInfo
    
    
    @property
    def numericSensorInfo(self):
        '''Health information provided by the power probes.
        '''
        return self.data['numericSensorInfo']

