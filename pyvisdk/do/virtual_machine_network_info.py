
from pyvisdk.do.virtual_machine_target_info import VirtualMachineTargetInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineNetworkInfo(VirtualMachineTargetInfo):
    '''NetworkInfo describes a network that a device backing can attached to.
    '''
    
    def __init__(self, network):
        # MUST define these
        super(VirtualMachineNetworkInfo, self).__init__()
    
        self.data['network'] = network
    
    
    @property
    def network(self):
        '''Information about the network
        '''
        return self.data['network']

