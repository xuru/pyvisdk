
from pyvisdk.do.vmware_distributed_virtual_switch_vlan_spec import VmwareDistributedVirtualSwitchVlanSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmwareDistributedVirtualSwitchTrunkVlanSpec(VmwareDistributedVirtualSwitchVlanSpec):
    '''This data type specifies that the port uses trunk mode, which allows the guest
        operating system to manage its own VLAN tags.
    '''
    
    def __init__(self, vlanId):
        # MUST define these
        super(VmwareDistributedVirtualSwitchTrunkVlanSpec, self).__init__()
    
        self.data['vlanId'] = vlanId
    
    
    @property
    def vlanId(self):
        '''The VlanId range for the trunk port. The valid VlanId range is from 0 to 4094.
        '''
        return self.data['vlanId']

