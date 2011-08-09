
from pyvisdk.do.virtual_device_device_backing_info import VirtualDeviceDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualPointingDeviceDeviceBackingInfo(VirtualDeviceDeviceBackingInfo):
    '''The VirtualPointingDevice.DeviceBackingInfo provides information about the
        physical mouse backing the VirtualPointingDevice data object type.
    '''
    
    def __init__(self, hostPointingDevice):
        # MUST define these
        super(VirtualPointingDeviceDeviceBackingInfo, self).__init__()
    
        self.data['hostPointingDevice'] = hostPointingDevice
    
    
    @property
    def hostPointingDevice(self):
        '''This optional property defines the mouse type (two-button, three-button, and so
        on). The mouse type determines how the user interacts with the host mouse.
        The valid values are specified in the VirtualPointingDeviceHostChoice
        list.
        '''
        return self.data['hostPointingDevice']

