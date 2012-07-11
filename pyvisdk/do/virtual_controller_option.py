
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualControllerOption(vim, *args, **kwargs):
    '''The VirtualControllerOption data object type contains information about a
    virtual controller type.'''
    
    obj = vim.client.factory.create('ns0:VirtualControllerOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'devices', 'deprecated', 'hotRemoveSupported', 'plugAndPlay', 'type' ]
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
    