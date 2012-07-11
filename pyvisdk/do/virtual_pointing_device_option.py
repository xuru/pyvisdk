
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPointingDeviceOption(vim, *args, **kwargs):
    '''The VirtualPointingDeviceOption data object type contains the options for the
    host mouse type defined in the VirtualPointingDevice data object type. These
    options include the valid selections for the mouse type, the supported mouse
    types, and the default mouse type.'''
    
    obj = vim.client.factory.create('ns0:VirtualPointingDeviceOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'deprecated', 'hotRemoveSupported', 'plugAndPlay', 'type' ]
    optional = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'licensingLimit', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    