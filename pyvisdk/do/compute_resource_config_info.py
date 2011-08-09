
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComputeResourceConfigInfo(DynamicData):
    '''Configuration of the compute resource; applies to both standalone hosts and
        clusters.
    '''
    
    def __init__(self, vmSwapPlacement):
        # MUST define these
        super(ComputeResourceConfigInfo, self).__init__()
    
        self.data['vmSwapPlacement'] = vmSwapPlacement
    
    
    @property
    def vmSwapPlacement(self):
        '''Swapfile placement policy for virtual machines within this compute resource. Any
        policy except for "inherit" is a valid value for this property; the
        default is "vmDirectory". This setting will be honored for each virtual
        machine within the compute resource for which the following is true: * The
        virtual machine is executing on a host that has the perVmSwapFiles
        capability. * The virtual machine configuration's swapPlacement property
        is set to "inherit".
        '''
        return self.data['vmSwapPlacement']

