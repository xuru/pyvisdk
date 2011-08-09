
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSCreateSpec(DynamicData):
    '''Specification to reconfigure a DistributedVirtualSwitch.
    '''
    
    def __init__(self, capability, configSpec, productInfo):
        # MUST define these
        super(DVSCreateSpec, self).__init__()
    
        self.data['capability'] = capability
        self.data['configSpec'] = configSpec
        self.data['productInfo'] = productInfo
    
    
    @property
    def capability(self):
        '''The capability of the switch.
        '''
        return self.data['capability']

    @property
    def configSpec(self):
        '''The configuration spec.
        '''
        return self.data['configSpec']

    @property
    def productInfo(self):
        '''The product information for the implementation of the switch.
        '''
        return self.data['productInfo']

