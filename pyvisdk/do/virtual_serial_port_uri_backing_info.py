
from pyvisdk.do.virtual_device_uri_backing_info import VirtualDeviceURIBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualSerialPortURIBackingInfo(VirtualDeviceURIBackingInfo):
    '''The data object specifies network backing for a . You can use URI backing to
        create a network serial port on the virtual machine, supporting
        connections between the virtual machine and remote systems.When a virtual
        machine establishes a connection with a remote system on the network, the
        virtual machine can act as a server or a client. When the virtual machine
        acts as a server, it accepts a connection. When the virtual machine acts
        as a client, it initiates the connection.You can configure the virtual
        serial port for communication through a virtual serial port concentrator
        that acts as a proxy between the virtual machine and the network. When you
        specify a , the virtual machine initiates the connection with the
        concentrator and forwards the and to the concentrator. For information
        about using a virtual serial port concentrator, see .ESX hosts support
        different protocols depending on your virtual serial port configuration.*
        If the virtual machine is handling the network connection directly (no
        specified), you can use telnet, TCP, and SSL protocols. The must use one
        of the following URI schemes:You cannot specify a username and password in
        the proxy URI. Any text following the port specification is ignored.For
        information about URI format, see .
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VirtualSerialPortURIBackingInfo, self).__init__()
    

    
    
