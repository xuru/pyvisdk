
from pyvisdk.do.virtual_device_device_backing_info import VirtualDeviceDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualSerialPortDeviceBackingInfo(VirtualDeviceDeviceBackingInfo):
    '''The data object defines information for using a host serial port device as backing
        for a . On a host, the first virtual machine to configure physical device
        backing for a virtual serial port will obtain the mapping. As long as that
        machine maintains the backing, any additional attempts to configure
        backing using that device will fail (a recoverable error, see the
        connection info ).
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VirtualSerialPortDeviceBackingInfo, self).__init__()
    

    
    
