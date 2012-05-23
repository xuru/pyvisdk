
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostResignatureRescanResult(vim, *args, **kwargs):
    '''When a user resignatures an UnresolvedVmfsVolume through DatastoreSystem API,
    we resignature and auto-mount on the other hosts which share the same
    underlying storage luns. As part of the operation, we rescan the specified list
    of hosts. This data object describes the return value of resignature APIs in
    DatastoreSystem.'''
    
    obj = vim.client.factory.create('ns0:HostResignatureRescanResult')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'result' ]
    optional = [ 'rescan', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    