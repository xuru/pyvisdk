
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNatService(DynamicData):
    '''A network address translation (NAT) service instance provides firewall and network
        address translation services for a virtual network.
    '''
    
    def __init__(self, key, spec):
        # MUST define these
        super(HostNatService, self).__init__()
    
        self.data['key'] = key
        self.data['spec'] = spec
    
    
    @property
    def key(self):
        '''The instance ID of the NAT service.
        '''
        return self.data['key']

    @property
    def spec(self):
        '''The configurable properties for the NatService object.
        '''
        return self.data['spec']

