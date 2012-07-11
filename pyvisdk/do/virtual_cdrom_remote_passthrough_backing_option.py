
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdromRemotePassthroughBackingOption(vim, *args, **kwargs):
    '''The VirtualCdromOption.RemotePassthroughBackingOption data object type contains
    the options for a remote pass-through CD-ROM device backing.Note that the
    server cannot present a list of valid remote backing devices because it is
    unable to scan remote hosts.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdromRemotePassthroughBackingOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'exclusive', 'autoDetectAvailable', 'type' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    