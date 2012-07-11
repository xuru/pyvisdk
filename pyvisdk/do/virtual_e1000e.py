
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualE1000e(vim, *args, **kwargs):
    '''The VirtualE1000e data object type represents an instance of the E1000e virtual
    Ethernet adapter attached to a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualE1000e')

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
    