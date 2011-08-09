
from pyvisdk.do.virtual_device_backing_info import VirtualDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceRemoteDeviceBackingInfo(VirtualDeviceBackingInfo):
    '''is a data object type for information about a remote device backing used by a
        device in a virtual machine. The primary difference between a remote
        device backing and a local device backing is that the VirtualCenter server
        cannot provide a list of remote host devices available for this virtual
        device backing.
    '''
    
    def __init__(self, deviceName, useAutoDetect):
        # MUST define these
        super(VirtualDeviceRemoteDeviceBackingInfo, self).__init__()
    
        self.data['deviceName'] = deviceName
        self.data['useAutoDetect'] = useAutoDetect
    
    
    @property
    def deviceName(self):
        '''The name of the device on the remote system.
        '''
        return self.data['deviceName']

    @property
    def useAutoDetect(self):
        '''Indicates whether the device should be auto detected instead of directly
        specified. If this value is set to TRUE,
        '''
        return self.data['useAutoDetect']

