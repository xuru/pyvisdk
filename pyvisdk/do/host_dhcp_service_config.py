
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDhcpServiceConfig(DynamicData):
    '''This data object type describes the configuration of a DHCP service instance
        representing both the configured properties on the instance and
        identification information.
    '''
    
    def __init__(self, changeOperation, key, spec):
        # MUST define these
        super(HostDhcpServiceConfig, self).__init__()
    
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
        '''The instance ID of the DHCP service.
        '''
        return self.data['key']

    @property
    def spec(self):
        '''Specification of the DHCP service.
        '''
        return self.data['spec']

