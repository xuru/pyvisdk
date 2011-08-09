
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVMotionNetConfig(DynamicData):
    '''The NetConfig data object type contains the networking configuration for VMotion
        operations.
    '''
    
    def __init__(self, candidateVnic, selectedVnic):
        # MUST define these
        super(HostVMotionNetConfig, self).__init__()
    
        self.data['candidateVnic'] = candidateVnic
        self.data['selectedVnic'] = selectedVnic
    
    
    @property
    def candidateVnic(self):
        '''List of VirtualNic objects that may be used for VMotion. This will be a subset of
        the list of VirtualNics in vnic.
        '''
        return self.data['candidateVnic']

    @property
    def selectedVnic(self):
        '''VirtualNic that is selected for use in VMotion operations.
        '''
        return self.data['selectedVnic']

