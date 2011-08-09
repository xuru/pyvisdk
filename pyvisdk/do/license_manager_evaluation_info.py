
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseManagerEvaluationInfo(DynamicData):
    '''Encapsulates product evaluation information
    '''
    
    def __init__(self, properties):
        # MUST define these
        super(LicenseManagerEvaluationInfo, self).__init__()
    
        self.data['properties'] = properties
    
    
    @property
    def properties(self):
        '''Evaluation properties
        '''
        return self.data['properties']

