
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualPort(vim, *args, **kwargs):
    '''The data object that represents a port in the distributed virtual switch.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualPort')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'config', 'conflict', 'dvsUuid', 'key', 'lastStatusChange' ]
    optional = [ 'conflictPortKey', 'connectee', 'connectionCookie', 'portgroupKey',
        'proxyHost', 'state', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    