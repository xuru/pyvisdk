
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSerialPort(vim, *args, **kwargs):
    '''The data object represents a serial port on a virtual machine. A virtual serial
    port uses one of the following backing types to specify how the virtual machine
    performs serial port operations.* Network backing ( ) supports a connection
    between the virtual machine and a resource on the network. The virtual machine
    can initiate a connection with the network resource, or it can listen for
    connections originating from the network. * Pipe backing ( ) supports I/O
    through a named pipe. The pipe connects the virtual machine to a host
    application or a virtual machine on the same host. * File backing ( ) supports
    output through the virtual serial port to a file on the same host. * Physical
    serial port backing ( ) supports a connection between the virtual machine and a
    device that is connected to a physical serial port on the host.When you use
    network backing, you can also configure a virtual serial port to use a virtual
    serial port concentrator. The virtual machine initiates a telnet connection
    with the concentrator, and the concentrator acts as a proxy between the virtual
    machine and a system on the network. By using a virtual serial port
    concentrator, you can maintain the connection between the virtual machine and
    the network resource when a vMotion event moves the virtual machine from one
    host to another. Without a virtual serial port concentrator, the connection
    would be lost. For information about using a serial port concentrator, see .You
    can configure a virtual serial port when you create or reconfigure a virtual
    machine. For example, to create a virtual serial port with network backing, use
    the following sequence of operations. In this procedure, the virtual serial
    port uses a proxy and will accept a network connection.If you use physical
    device backing ( ), you should also use the method to determine if a serial
    device is available before configuring device backing.'''
    
    obj = vim.client.factory.create('ns0:VirtualSerialPort')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'yieldOnPoll', 'key' ]
    optional = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'unitNumber',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    