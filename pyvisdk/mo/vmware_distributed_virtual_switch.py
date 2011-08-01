
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.distributed_virtual_switch import DistributedVirtualSwitch
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmwareDistributedVirtualSwitch(DistributedVirtualSwitch):
    '''The interface to the VMware implementation of the switch. The functionality listed
        here is for VMware DistributedVirtualSwitch only.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.VmwareDistributedVirtualSwitch):
        # MUST define these
        super(VmwareDistributedVirtualSwitch, self).__init__(core, name=name, ref=ref, type=type)
    
    
