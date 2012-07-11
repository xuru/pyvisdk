
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPS2ControllerOption(vim, *args, **kwargs):
    '''The VirtualPS2ControllerOption data object type contains the options for a
    virtual PS/2 controller for keyboards and mice. In addition to the options
    defined in the VirtualControllerOption data object type, these options include
    the number of keyboards and mice.'''
    
    obj = vim.client.factory.create('ns0:VirtualPS2ControllerOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'numKeyboards', 'numPointingDevices', 'devices', 'deprecated',
        'hotRemoveSupported', 'plugAndPlay', 'type' ]
    optional = [ 'supportedDevice', 'autoAssignController', 'backingOption', 'connectOption',
        'controllerType', 'defaultBackingOptionIndex', 'licensingLimit',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    