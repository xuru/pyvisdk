
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualController(vim, *args, **kwargs):
    '''VirtualController is the base data object type for a device controller in a
    virtual machine. VirtualController extends VirtualDevice to inherit general
    information about a controller (such as name and description), and to allow
    controllers to appear in a generic list of virtual devices.'''
    
    obj = vim.client.factory.create('ns0:VirtualController')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'busNumber', 'key' ]
    optional = [ 'device', 'backing', 'connectable', 'controllerKey', 'deviceInfo',
        'unitNumber', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    