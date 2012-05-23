
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchManagerHostContainer(vim, *args, **kwargs):
    '''Check host compatibility for all hosts in the container. If the recursive flag
    is true, then check hosts at all levels within this container, otherwise check
    only at the container level. In case of container being a Datacenter, the
    recursive flag is applied to its HostFolder.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchManagerHostContainer')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'container', 'recursive' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    