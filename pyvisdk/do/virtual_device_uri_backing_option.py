
from pyvisdk.do.virtual_device_backing_option import VirtualDeviceBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceURIBackingOption(VirtualDeviceBackingOption):
    '''The URIBackingOption data object type describes network communication options for
        virtual devices. When establishing a connection with a remote system on
        the network, the virtual machine can act as a server or a client. When the
        virtual machine acts as a server, it accepts a connection. When the
        virtual machine acts as a client, it initiates the connection.
    '''
    
    def __init__(self, directions):
        # MUST define these
        super(VirtualDeviceURIBackingOption, self).__init__()
    
        self.data['directions'] = directions
    
    
    @property
    def directions(self):
        '''List of possible directions. Valid directions are: * server * client
        '''
        return self.data['directions']

