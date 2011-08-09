
from pyvisdk.do.virtual_device_pipe_backing_info import VirtualDevicePipeBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualSerialPortPipeBackingInfo(VirtualDevicePipeBackingInfo):
    '''The data object defines information for backing a with a named pipe. You can use a
        pipe to connect a virtual serial port to a host application or to another
        virtual machine on the host computer. This is useful for capturing
        debugging information sent through the virtual serial port.
    '''
    
    def __init__(self, endpoint, noRxLoss):
        # MUST define these
        super(VirtualSerialPortPipeBackingInfo, self).__init__()
    
        self.data['endpoint'] = endpoint
        self.data['noRxLoss'] = noRxLoss
    
    
    @property
    def endpoint(self):
        '''Indicates the role the virtual machine assumes as an endpoint for the pipe. The
        valid values are "client" or "server".
        '''
        return self.data['endpoint']

    @property
    def noRxLoss(self):
        '''Enables optimized data transfer over the pipe. When you use this feature, the ESX
        server buffers data to prevent data overrun. This allows the virtual
        machine to read all of the data transferred over the pipe with no data
        loss. To use optimized data transfer, set
        '''
        return self.data['noRxLoss']

