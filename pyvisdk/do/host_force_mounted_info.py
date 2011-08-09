
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostForceMountedInfo(DynamicData):
    '''When the system detects a copy of a VmfsVolume, it will not be auto-mounted on the
        host and it will be detected as 'UnresolvedVmfsVolume'. If user decides to
        keep the original Uuid and mount it on the host, it will have
        'forceMounted' flag and 'forceMountedInfo' set. 'ForceMountedInfo'
        provides additional information specific to user-mounted VmfsVolume.
    '''
    
    def __init__(self, mounted, persist):
        # MUST define these
        super(HostForceMountedInfo, self).__init__()
    
        self.data['mounted'] = mounted
        self.data['persist'] = persist
    
    
    @property
    def mounted(self):
        '''Indicates if the volume is currently mounted on the host
        '''
        return self.data['mounted']

    @property
    def persist(self):
        '''Indicates if the vmfsExtent information persistent across host reboots.
        '''
        return self.data['persist']

