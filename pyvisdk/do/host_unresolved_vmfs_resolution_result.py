
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostUnresolvedVmfsResolutionResult(DynamicData):
    '''When an UnresolvedVmfsVolume has been resignatured or forceMounted, we want to
        return the original spec information along with newly created VMFS volume.
    '''
    
    def __init__(self, fault, spec, vmfs):
        # MUST define these
        super(HostUnresolvedVmfsResolutionResult, self).__init__()
    
        self.data['fault'] = fault
        self.data['spec'] = spec
        self.data['vmfs'] = vmfs
    
    
    @property
    def fault(self):
        ''''fault' would be set if the operation was not successful
        '''
        return self.data['fault']

    @property
    def spec(self):
        '''The original UnresolvedVmfsResolutionSpec which user had specified
        '''
        return self.data['spec']

    @property
    def vmfs(self):
        '''Newly created VmfsVolume
        '''
        return self.data['vmfs']

