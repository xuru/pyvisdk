
from pyvisdk.do.physical_nic_hint import PhysicalNicHint
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicNameHint(PhysicalNicHint):
    '''This data object type describes a network in network hint where the network
        describes the color, label, or the name of the network.
    '''
    
    def __init__(self, network):
        # MUST define these
        super(PhysicalNicNameHint, self).__init__()
    
        self.data['network'] = network
    
    
    @property
    def network(self):
        '''The network name.
        '''
        return self.data['network']

