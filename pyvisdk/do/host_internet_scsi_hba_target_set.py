
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaTargetSet(DynamicData):
    '''A collection of one or more static targets or discovery addresses. At least one of
        the arrays must be non-empty.
    '''
    
    def __init__(self, sendTargets, staticTargets):
        # MUST define these
        super(HostInternetScsiHbaTargetSet, self).__init__()
    
        self.data['sendTargets'] = sendTargets
        self.data['staticTargets'] = staticTargets
    
    
    @property
    def sendTargets(self):
        '''
        '''
        return self.data['sendTargets']

    @property
    def staticTargets(self):
        '''
        '''
        return self.data['staticTargets']

