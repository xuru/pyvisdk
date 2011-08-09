
from pyvisdk.do.virtual_device_backing_info import VirtualDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDevicePipeBackingInfo(VirtualDeviceBackingInfo):
    '''The data object type defines information for using a named pipe as backing for a
        device in a virtual machine.
    '''
    
    def __init__(self, pipeName):
        # MUST define these
        super(VirtualDevicePipeBackingInfo, self).__init__()
    
        self.data['pipeName'] = pipeName
    
    
    @property
    def pipeName(self):
        '''Pipe name for the host pipe associated with this backing.
        '''
        return self.data['pipeName']

