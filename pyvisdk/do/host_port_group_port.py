
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPortGroupPort(vim, *args, **kwargs):
    '''A Port data object type is a runtime representation of network connectivity
    between a network service or virtual machine and a virtual switch. This is
    different from a port group in that the port group represents the configuration
    aspects of the network connection. The Port object provides runtime statistics.'''
    
    obj = vim.client.factory.create('ns0:HostPortGroupPort')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'type' ]
    optional = [ 'key', 'mac', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    