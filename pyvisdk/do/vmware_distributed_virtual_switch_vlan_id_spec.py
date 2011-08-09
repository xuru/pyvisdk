
from pyvisdk.do.vmware_distributed_virtual_switch_vlan_spec import VmwareDistributedVirtualSwitchVlanSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmwareDistributedVirtualSwitchVlanIdSpec(VmwareDistributedVirtualSwitchVlanSpec):
    '''This data type defines the configuration when single vlanId is used for the port.
    '''
    
    def __init__(self, vlanId):
        # MUST define these
        super(VmwareDistributedVirtualSwitchVlanIdSpec, self).__init__()
    
        self.data['vlanId'] = vlanId
    
    
    @property
    def vlanId(self):
        '''The VLAN ID for ports. Possible values: * A value of 0 specifies that you do not
        want the port associated with a VLAN. * A value from 1 to 4094 specifies a
        VLAN ID for the port.
        '''
        return self.data['vlanId']

