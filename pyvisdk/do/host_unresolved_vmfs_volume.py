
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostUnresolvedVmfsVolume(vim, *args, **kwargs):
    '''Information about detected unbound, unresolved VMFS volume. An unresolved VMFS
    volume is reported when one or more device partitions of volume are detected to
    have copies of extents of the volume. Such copies can be created via
    replication or snapshots.UnresolvedVmfsVolume are not mounted on the host where
    they are detected. User may choose to resignature the volume in which case a
    new Uuid is assigned to the volume and contents of the VMFS volume is kept
    intact.User may choose to keep the original Uuid and mount the VMFS volume as
    it is on the given host. In this case, user has choosen to mount the copy of
    the VMFS volume on that host with no change to the original Uuid. This may fail
    with VmfsVolumeAlreadyMounted exception if there is an existing VMFS volume
    with the same Uuid mounted somewhere in the same datacenter.Simple diagram
    representing the possible operations on UnresolvedVmfsVolumeSee
    HostStorageSystem'''
    
    obj = vim.client.factory.create('ns0:HostUnresolvedVmfsVolume')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'extent', 'resolveStatus', 'totalBlocks', 'vmfsLabel', 'vmfsUuid' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    