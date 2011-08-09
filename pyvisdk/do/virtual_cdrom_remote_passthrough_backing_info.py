
from pyvisdk.do.virtual_device_remote_device_backing_info import VirtualDeviceRemoteDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualCdromRemotePassthroughBackingInfo(VirtualDeviceRemoteDeviceBackingInfo):
    '''The VirtualCdrom.RemotePassthroughBackingInfo data object type contains the
        information to specify a remote pass-through device backing of a virtual
        CD-ROM.
    '''
    
    def __init__(self, exclusive):
        # MUST define these
        super(VirtualCdromRemotePassthroughBackingInfo, self).__init__()
    
        self.data['exclusive'] = exclusive
    
    
    @property
    def exclusive(self):
        '''Flag to indicate whether or not the virtual machine has exclusive access to the
        CD-ROM device.
        '''
        return self.data['exclusive']

