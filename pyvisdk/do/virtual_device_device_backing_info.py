
from pyvisdk.do.virtual_device_backing_info import VirtualDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceDeviceBackingInfo(VirtualDeviceBackingInfo):
    '''The data object type defines information about a host device or resource that
        backs a device in a virtual machine.
    '''
    
    def __init__(self, deviceName, useAutoDetect):
        # MUST define these
        super(VirtualDeviceDeviceBackingInfo, self).__init__()
    
        self.data['deviceName'] = deviceName
        self.data['useAutoDetect'] = useAutoDetect
    
    
    @property
    def deviceName(self):
        '''The name of the device on the host system.
        '''
        return self.data['deviceName']

    @property
    def useAutoDetect(self):
        '''Indicates whether the device should be auto detected instead of directly
        specified. If this value is set to TRUE, deviceName is ignored.
        '''
        return self.data['useAutoDetect']

