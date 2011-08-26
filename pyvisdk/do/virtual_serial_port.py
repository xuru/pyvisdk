
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSerialPort(vim, *args, **kwargs):
    '''When you use network backing, you can also configure a virtual serial port to
    use a virtual serial port concentrator. The virtual machine initiates a telnet
    connection with the concentrator, and the concentrator acts as a proxy between
    the virtual machine and a system on the network. By using a virtual serial port
    concentrator, you can maintain the connection between the virtual machine and
    the network resource when a vMotion event moves the virtual machine from one
    host to another. Without a virtual serial port concentrator, the connection
    would be lost. For information about using a serial port concentrator, see .You
    can configure a virtual serial port when you create or reconfigure a virtual
    machine. For example, to create a virtual serial port with network backing, use
    the following sequence of operations. In this procedure, the virtual serial
    port uses a proxy and will accept a network connection.'''
    
    obj = vim.client.factory.create('ns0:VirtualSerialPort')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'key', 'yieldOnPoll' ]
    inherited = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'unitNumber' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    