
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDevice(DynamicData):
    '''This data object type defines a device on the host.
    '''
    
    def __init__(self, deviceName, deviceType):
        # MUST define these
        super(HostDevice, self).__init__()
    
        self.data['deviceName'] = deviceName
        self.data['deviceType'] = deviceType
    
    
    @property
    def deviceName(self):
        '''The name of the device on the host. For example, /dev/cdrom or
        \\serverX\device_name.
        '''
        return self.data['deviceName']

    @property
    def deviceType(self):
        '''Device type when available: floppy, mouse, cdrom, disk, scsi device, or adapter.
        '''
        return self.data['deviceType']

