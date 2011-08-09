
from pyvisdk.do.physical_nic_hint import PhysicalNicHint
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicIpHint(PhysicalNicHint):
    '''This data object type describes a network in network hint where the network is
        specified using IP addresses, for example, 10.27.49.1-10.27.49.254
    '''
    
    def __init__(self, ipSubnet):
        # MUST define these
        super(PhysicalNicIpHint, self).__init__()
    
        self.data['ipSubnet'] = ipSubnet
    
    
    @property
    def ipSubnet(self):
        '''The network IP addresses.
        '''
        return self.data['ipSubnet']

