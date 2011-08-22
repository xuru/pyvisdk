
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPointingDeviceDeviceBackingInfo(vim, *args, **kwargs):
    '''The VirtualPointingDevice.DeviceBackingInfo provides information about the
    physical mouse backing the VirtualPointingDevice data object type.'''
    
    obj = vim.client.factory.create('ns0:VirtualPointingDeviceDeviceBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'deviceName', 'hostPointingDevice' ]
    inherited = [ 'useAutoDetect' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    