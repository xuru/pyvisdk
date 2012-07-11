
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNicLinkInfo(vim, *args, **kwargs):
    '''The PhysicalNicLinkInfo data object describes the link speed and the type of
    duplex communication. The link speed indicates the bit rate in megabits per
    second. The duplex boolean indicates if the link is capable of full-duplex or
    half-duplex communication.'''
    
    obj = vim.client.factory.create('ns0:PhysicalNicLinkInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'duplex', 'speedMb' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    