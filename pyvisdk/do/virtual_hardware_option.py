
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualHardwareOption(vim, *args, **kwargs):
    '''The VirtualHardwareOption data object contains the options available for all
    virtual devices.'''
    
    obj = vim.client.factory.create('ns0:VirtualHardwareOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 14:
        raise IndexError('Expected at least 15 arguments got: %d' % len(args))

    required = [ 'deviceListReadonly', 'hwVersion', 'memoryMB', 'numCoresPerSocket', 'numCPU',
        'numCpuReadonly', 'numIDEControllers', 'numPCIControllers',
        'numPS2Controllers', 'numSIOControllers', 'numUSBControllers',
        'numUSBXHCIControllers', 'resourceConfigOption', 'virtualDeviceOption' ]
    optional = [ 'licensingLimit', 'numSupportedWwnNodes', 'numSupportedWwnPorts',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    