
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNatServiceConfig(DynamicData):
    '''This data object type describes the network address translation (NAT) service
        configuration representing both the configured properties on a NAT Service
        and identification information.
    '''
    
    def __init__(self, changeOperation, key, spec):
        # MUST define these
        super(HostNatServiceConfig, self).__init__()
    
        self.data['changeOperation'] = changeOperation
        self.data['key'] = key
        self.data['spec'] = spec
    
    
    @property
    def changeOperation(self):
        '''Indicates the change operation to apply on this configuration specification.
        '''
        return self.data['changeOperation']

    @property
    def key(self):
        '''The instance ID of the NAT service.
        '''
        return self.data['key']

    @property
    def spec(self):
        '''The specification of the NAT service.
        '''
        return self.data['spec']

