
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskSparseVer1BackingInfo(vim, *args, **kwargs):
    '''This data object type contains information about backing a virtual disk by
    using a virtual disk file on the host, in the sparse disk format used by GSX
    Server 2.x.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskSparseVer1BackingInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'diskMode', 'fileName' ]
    optional = [ 'contentId', 'parent', 'spaceUsedInKB', 'split', 'writeThrough', 'datastore',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    