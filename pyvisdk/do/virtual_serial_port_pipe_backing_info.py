
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSerialPortPipeBackingInfo(vim, *args, **kwargs):
    '''The data object defines information for backing a with a named pipe. You can
    use a pipe to connect a virtual serial port to a host application or to another
    virtual machine on the host computer. This is useful for capturing debugging
    information sent through the virtual serial port.'''
    
    obj = vim.client.factory.create('ns0:VirtualSerialPortPipeBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'pipeName', 'endpoint' ]
    inherited = [ 'noRxLoss' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    