
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileDeferredPolicyOptionParameter(DynamicData):
    '''DataObject which contains information about one Deferred parameter. User can fill
        in the deferred parameters at apply time.
    '''
    
    def __init__(self, inputPath, parameter):
        # MUST define these
        super(ProfileDeferredPolicyOptionParameter, self).__init__()
    
        self.data['inputPath'] = inputPath
        self.data['parameter'] = parameter
    
    
    @property
    def inputPath(self):
        '''Complete path to the Policy for which the User input is specified.
        '''
        return self.data['inputPath']

    @property
    def parameter(self):
        '''Parameters that needed userInput.
        '''
        return self.data['parameter']

