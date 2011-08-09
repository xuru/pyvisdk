
from pyvisdk.do.virtual_device_device_backing_info import VirtualDeviceDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualCdromPassthroughBackingInfo(VirtualDeviceDeviceBackingInfo):
    '''The VirtualCdrom.PassthroughBackingInfo data class represents a device pass-
        through backing for a virtual CD-ROM.
    '''
    
    def __init__(self, exclusive):
        # MUST define these
        super(VirtualCdromPassthroughBackingInfo, self).__init__()
    
        self.data['exclusive'] = exclusive
    
    
    @property
    def exclusive(self):
        '''Flag to indicate whether or not the virtual machine has exclusive CD-ROM device
        access.
        '''
        return self.data['exclusive']

