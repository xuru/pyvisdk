
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNasVolumeConfig(DynamicData):
    '''This describes the NAS Volume configuration containing the configurable properties
        on a NAS Volume
    '''
    
    def __init__(self, changeOperation, spec):
        # MUST define these
        super(HostNasVolumeConfig, self).__init__()
    
        self.data['changeOperation'] = changeOperation
        self.data['spec'] = spec
    
    
    @property
    def changeOperation(self):
        '''Indicates the change operation to apply on this configuration specification.
        '''
        return self.data['changeOperation']

    @property
    def spec(self):
        '''The specification volume.
        '''
        return self.data['spec']

