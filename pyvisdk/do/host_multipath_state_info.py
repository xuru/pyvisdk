
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathStateInfo(vim, *args, **kwargs):
    '''This data object type describes the state of storage paths on the host. All
    storage paths on the host are enumerated in this data object.The reason all
    path state information is encapsulated in this data object is because the path
    may actively change. This data object ensures that a request to gather path
    state changes only needs to fetch this data object.'''
    
    obj = vim.client.factory.create('ns0:HostMultipathStateInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'path', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    