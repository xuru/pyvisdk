
from pyvisdk.do.distributed_virtual_switch_host_member_backing import DistributedVirtualSwitchHostMemberBacking
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchHostMemberPnicBacking(DistributedVirtualSwitchHostMemberBacking):
    '''Specification to select individual physical NICs. In this case, a proxy switch
        will be created on the host from scratch with the pNICs as the uplinks.
    '''
    
    def __init__(self, pnicSpec):
        # MUST define these
        super(DistributedVirtualSwitchHostMemberPnicBacking, self).__init__()
    
        self.data['pnicSpec'] = pnicSpec
    
    
    @property
    def pnicSpec(self):
        '''The key of the physical NICs to be added in the switch.
        '''
        return self.data['pnicSpec']

