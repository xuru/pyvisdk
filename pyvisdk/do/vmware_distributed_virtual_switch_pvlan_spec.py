
from pyvisdk.do.vmware_distributed_virtual_switch_vlan_spec import VmwareDistributedVirtualSwitchVlanSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmwareDistributedVirtualSwitchPvlanSpec(VmwareDistributedVirtualSwitchVlanSpec):
    '''This data type defines the configuration when PVLAN id is to be used for the
        ports.
    '''
    
    def __init__(self, pvlanId):
        # MUST define these
        super(VmwareDistributedVirtualSwitchPvlanSpec, self).__init__()
    
        self.data['pvlanId'] = pvlanId
    
    
    @property
    def pvlanId(self):
        '''The secondaryVlanId.
        '''
        return self.data['pvlanId']

