
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSerialPortURIBackingInfo(vim, *args, **kwargs):
    '''The data object specifies network backing for a . You can use URI backing to
    create a network serial port on the virtual machine, supporting connections
    between the virtual machine and remote systems.When a virtual machine
    establishes a connection with a remote system on the network, the virtual
    machine can act as a server or a client. When the virtual machine acts as a
    server, it accepts a connection. When the virtual machine acts as a client, it
    initiates the connection.You can configure the virtual serial port for
    communication through a virtual serial port concentrator that acts as a proxy
    between the virtual machine and the network. When you specify a , the virtual
    machine initiates the connection with the concentrator and forwards the and to
    the concentrator. For information about using a virtual serial port
    concentrator, see .ESX hosts support different protocols depending on your
    virtual serial port configuration.* If the virtual machine is handling the
    network connection directly (no specified), you can use telnet, TCP, and SSL
    protocols. The must use one of the following URI schemes:You cannot specify a
    username and password in the proxy URI. Any text following the port
    specification is ignored.For information about URI format, see .'''
    
    obj = vim.client.factory.create('ns0:VirtualSerialPortURIBackingInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'direction', 'serviceURI' ]
    optional = [ 'proxyURI', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    