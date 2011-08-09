
from pyvisdk.do.virtual_device_backing_option import VirtualDeviceBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceRemoteDeviceBackingOption(VirtualDeviceBackingOption):
    '''VirtualDeviceOption.RemoteDeviceBackingOption describes the options for a remote
        device backing. The primary difference between a remote device backing and
        a local device backing is that the VirtualCenter server cannot provide a
        list of remote host devices available for this virtual device backing.
    '''
    
    def __init__(self, autoDetectAvailable):
        # MUST define these
        super(VirtualDeviceRemoteDeviceBackingOption, self).__init__()
    
        self.data['autoDetectAvailable'] = autoDetectAvailable
    
    
    @property
    def autoDetectAvailable(self):
        '''Flag to indicate whether the specific instance of this device can be auto-detected
        on the host instead of having to specify a particular physical device.
        '''
        return self.data['autoDetectAvailable']

