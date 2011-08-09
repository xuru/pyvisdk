
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComputeResourceConfigSpec(DynamicData):
    '''Changes to apply to the compute resource configuration.
    '''
    
    def __init__(self, vmSwapPlacement):
        # MUST define these
        super(ComputeResourceConfigSpec, self).__init__()
    
        self.data['vmSwapPlacement'] = vmSwapPlacement
    
    
    @property
    def vmSwapPlacement(self):
        '''New setting for the swapfile placement policy. Any change to this policy will
        affect virtual machines that subsequently power on or resume from a
        suspended state in this compute resource, or that migrate to a host in
        this compute resource while powered on; virtual machines that are
        currently powered on in this compute resource will not yet be affected.
        '''
        return self.data['vmSwapPlacement']

