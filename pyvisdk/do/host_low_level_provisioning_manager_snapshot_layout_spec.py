
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostLowLevelProvisioningManagerSnapshotLayoutSpec(vim, *args, **kwargs):
    '''File layout spec of a snapshot, including path to the vmsn file of the snapshot
    and the layout of virtual disks when the snapshot was taken.'''
    
    obj = vim.client.factory.create('ns0:HostLowLevelProvisioningManagerSnapshotLayoutSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'dstFilename', 'id', 'srcFilename' ]
    optional = [ 'disk', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    