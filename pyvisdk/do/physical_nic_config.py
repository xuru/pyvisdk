
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicConfig(DynamicData):
    '''The configuration of the physical network adapter containing both the configurable
        properties and identification information.
    '''
    
    def __init__(self, device, spec):
        # MUST define these
        super(PhysicalNicConfig, self).__init__()
    
        self.data['device'] = device
        self.data['spec'] = spec
    
    
    @property
    def device(self):
        '''PhysicalNic device to which configuration applies.
        '''
        return self.data['device']

    @property
    def spec(self):
        '''The specification of the physical network adapter.
        '''
        return self.data['spec']

