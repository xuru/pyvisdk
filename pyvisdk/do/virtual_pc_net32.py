
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPCNet32(vim, *args, **kwargs):
    '''This data object type defines the properties of an AMD Lance PCNet32 Ethernet
    card attached to a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualPCNet32')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'key' ]
    optional = [ 'addressType', 'macAddress', 'wakeOnLanEnabled', 'backing', 'connectable',
        'controllerKey', 'deviceInfo', 'unitNumber', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    