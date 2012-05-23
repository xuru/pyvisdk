
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFibreChannelHba(vim, *args, **kwargs):
    '''This data object type describes the Fibre Channel host bus adapter.'''
    
    obj = vim.client.factory.create('ns0:HostFibreChannelHba')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 8:
        raise IndexError('Expected at least 9 arguments got: %d' % len(args))

    required = [ 'nodeWorldWideName', 'portType', 'portWorldWideName', 'speed', 'bus', 'device',
        'model', 'status' ]
    optional = [ 'driver', 'key', 'pci', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    