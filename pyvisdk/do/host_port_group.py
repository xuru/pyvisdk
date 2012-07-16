
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPortGroup(vim, *args, **kwargs):
    '''This data object type is used to describe port groups. Port groups are used to
    group virtual network adapters on a virtual switch, associating them with
    networks and network policies.'''
    
    obj = vim.client.factory.create('ns0:HostPortGroup')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'computedPolicy', 'spec' ]
    optional = [ 'key', 'port', 'vswitch', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    