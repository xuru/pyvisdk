
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSerialPortDeviceBackingInfo(vim, *args, **kwargs):
    '''The data object defines information for using a host serial port device as
    backing for a . On a host, the first virtual machine to configure physical
    device backing for a virtual serial port will obtain the mapping. As long as
    that machine maintains the backing, any additional attempts to configure
    backing using that device will fail (a recoverable error, see the connection
    info ).'''
    
    obj = vim.client.factory.create('ns0:VirtualSerialPortDeviceBackingInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'deviceName' ]
    optional = [ 'useAutoDetect', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    