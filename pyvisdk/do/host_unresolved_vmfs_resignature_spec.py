
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostUnresolvedVmfsResignatureSpec(DynamicData):
    '''Specification to resignature an Unresolved VMFS volume.
    '''
    
    def __init__(self, extentDevicePath):
        # MUST define these
        super(HostUnresolvedVmfsResignatureSpec, self).__init__()
    
        self.data['extentDevicePath'] = extentDevicePath
    
    
    @property
    def extentDevicePath(self):
        '''List of device path each specifying VMFS extents.
        '''
        return self.data['extentDevicePath']

