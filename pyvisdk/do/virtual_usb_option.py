# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualUSBOption(vim, *args, **kwargs):
    '''The VirtualUSBOption data object type contains options for USB device
    configuration on a virtual machine. The vSphere API supports the following
    options:* Local host USB connection (VirtualUSBUSBBackingOption) * Remote host
    USB connection (VirtualUSBRemoteHostBackingOption)For information about USB
    device configuration, see VirtualUSB.'''
    
    obj = vim.client.factory.create('ns0:VirtualUSBOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    