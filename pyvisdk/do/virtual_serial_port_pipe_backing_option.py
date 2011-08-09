
from pyvisdk.do.virtual_device_pipe_backing_option import VirtualDevicePipeBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualSerialPortPipeBackingOption(VirtualDevicePipeBackingOption):
    '''The data object contains the options for backing a serial port device with a pipe
        to another process.
    '''
    
    def __init__(self, endpoint, noRxLoss):
        # MUST define these
        super(VirtualSerialPortPipeBackingOption, self).__init__()
    
        self.data['endpoint'] = endpoint
        self.data['noRxLoss'] = noRxLoss
    
    
    @property
    def endpoint(self):
        '''Indicates the choices available and the default setting for the pipe endpoint. As
        an endpoint, the virtual machine can act as a client or a server.
        '''
        return self.data['endpoint']

    @property
    def noRxLoss(self):
        '''Indicates whether the server supports optimized data transfer over the pipe and
        also specifies default behavior.
        '''
        return self.data['noRxLoss']

