
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostUnresolvedVmfsExtent(vim, *args, **kwargs):
    '''Information about an unresolved VMFS volume extent An unresolved VMFS volume
    extent is a device partition which is detected to have copy of an extent of a
    VMFS volume. Such a copy can be created via replication or snapshots, for
    example.See HostUnresolvedVmfsVolume'''
    
    obj = vim.client.factory.create('ns0:HostUnresolvedVmfsExtent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 8:
        raise IndexError('Expected at least 9 arguments got: %d' % len(args))

    required = [ 'device', 'devicePath', 'endBlock', 'isHeadExtent', 'ordinal', 'reason',
        'startBlock', 'vmfsUuid' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    