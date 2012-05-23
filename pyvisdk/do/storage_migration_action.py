
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StorageMigrationAction(vim, *args, **kwargs):
    '''Describes a single storage migration action. The storage migration action
    applies either to a virtual machine or a set of virtual disks.NOTE: This data
    object type and all of its methods are experimental and subject to change in
    future releases.'''
    
    obj = vim.client.factory.create('ns0:StorageMigrationAction')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'destination', 'relocateSpec', 'sizeTransferred', 'source', 'vm', 'type' ]
    optional = [ 'ioLatencyDstBefore', 'ioLatencySrcBefore', 'spaceUtilDstAfter',
        'spaceUtilDstBefore', 'spaceUtilSrcAfter', 'spaceUtilSrcBefore', 'target',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    