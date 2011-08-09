
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostLicenseConnectInfo(DynamicData):
    '''This data object type describes license information stored on the host.
    '''
    
    def __init__(self, evaluation, license):
        # MUST define these
        super(HostLicenseConnectInfo, self).__init__()
    
        self.data['evaluation'] = evaluation
        self.data['license'] = license
    
    
    @property
    def evaluation(self):
        '''Evaluation information.
        '''
        return self.data['evaluation']

    @property
    def license(self):
        '''License information.
        '''
        return self.data['license']

