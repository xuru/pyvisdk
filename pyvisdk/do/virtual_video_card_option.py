
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualVideoCardOption(vim, *args, **kwargs):
    '''This data object type contains the options for the VirtualVideoCard data object
    type.'''
    
    obj = vim.client.factory.create('ns0:VirtualVideoCardOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'deprecated', 'hotRemoveSupported', 'plugAndPlay', 'type' ]
    optional = [ 'numDisplays', 'support3D', 'useAutoDetect', 'videoRamSizeInKB',
        'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'licensingLimit', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    