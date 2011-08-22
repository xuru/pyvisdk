
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceOption(vim, *args, **kwargs):
    '''The VirtualDeviceOption data object type contains information about a virtual
    device type, the options for configuring the virtual device, and the
    relationship between this virtual device and other devices. The vSphere API
    groups device configurations that are mutually exclusive into different
    configuration objects; each of these configuration objects may define subtypes
    for virtual device backing options that are independent of the virtual device.
    Backing-dependent options should appear in a subtype of
    VirtualDeviceBackingOption.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'deprecated', 'hotRemoveSupported', 'plugAndPlay', 'type' ]
    inherited = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'licensingLimit' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    