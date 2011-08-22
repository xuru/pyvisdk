
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
    if (len(args) + len(kwargs)) < 12:
        raise IndexError('Expected at least 13 arguments got: %d' % len(args))
        
    signature = [ 'deviceListReadonly', 'hwVersion', 'memoryMB', 'numCPU', 'numCpuReadonly',
        'numIDEControllers', 'numPCIControllers', 'numPS2Controllers',
        'numSIOControllers', 'numUSBControllers', 'resourceConfigOption',
        'virtualDeviceOption' ]
    inherited = [ 'licensingLimit', 'numSupportedWwnNodes', 'numSupportedWwnPorts' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    