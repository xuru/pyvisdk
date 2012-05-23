
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdromRemotePassthroughBackingInfo(vim, *args, **kwargs):
    '''The VirtualCdrom.RemotePassthroughBackingInfo data object type contains the
    information to specify a remote pass-through device backing of a virtual CD-
    ROM.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdromRemotePassthroughBackingInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'exclusive', 'deviceName' ]
    optional = [ 'useAutoDetect', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    