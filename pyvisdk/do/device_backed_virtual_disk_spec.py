
from pyvisdk.do.virtual_disk_spec import VirtualDiskSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DeviceBackedVirtualDiskSpec(VirtualDiskSpec):
    '''Specification used to create a host device backed virtual disk
    '''
    
    def __init__(self, device):
        # MUST define these
        super(DeviceBackedVirtualDiskSpec, self).__init__()
    
        self.data['device'] = device
    
    
    @property
    def device(self):
        '''The deviceName of the backing device
        '''
        return self.data['device']

