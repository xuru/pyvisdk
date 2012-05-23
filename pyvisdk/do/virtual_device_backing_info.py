
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceBackingInfo(vim, *args, **kwargs):
    '''is a base data object type for information about the backing of a device in a
    virtual machine. This base type does not define any properties. It is used as a
    namespace for general-purpose subtypes. Specific devices are represented by
    subtypes which define properties for device-specific backing information.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceBackingInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    