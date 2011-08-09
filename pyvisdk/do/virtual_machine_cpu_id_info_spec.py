
from pyvisdk.do.array_update_spec import ArrayUpdateSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineCpuIdInfoSpec(ArrayUpdateSpec):
    '''Wrapper class to support incremental updates of the cpuFeatureMask.
    '''
    
    def __init__(self, info):
        # MUST define these
        super(VirtualMachineCpuIdInfoSpec, self).__init__()
    
        self.data['info'] = info
    
    
    @property
    def info(self):
        '''
        '''
        return self.data['info']

