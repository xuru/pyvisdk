
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchHostProductSpec(DynamicData):
    '''This data object type is a subset of AboutInfo. An object of this type can be used
        to describe the specification for a host.
    '''
    
    def __init__(self, productLineId, version):
        # MUST define these
        super(DistributedVirtualSwitchHostProductSpec, self).__init__()
    
        self.data['productLineId'] = productLineId
        self.data['version'] = version
    
    
    @property
    def productLineId(self):
        '''The product-line name.
        '''
        return self.data['productLineId']

    @property
    def version(self):
        '''Dot-separated version string. For example, "1.2".
        '''
        return self.data['version']

