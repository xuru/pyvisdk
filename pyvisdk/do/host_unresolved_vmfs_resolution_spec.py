
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostUnresolvedVmfsResolutionSpec(vim, *args, **kwargs):
    '''An unresolved VMFS volume is reported when one or more device partitions of
    volume are detected to have copies of extents of the volume. Such copies can be
    created via replication or snapshots, for example. This data object type
    describes how to resolve an unbound VMFS volume. The SCSI device path for each
    of the VMFS volume extent should be specified. For the current release, only
    head-extent needs to be specified. In future releases, we will allow user to
    specify explicitly all the extents which makes up a new Vmfs Volume.'''
    
    obj = vim.client.factory.create('ns0:HostUnresolvedVmfsResolutionSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'extentDevicePath', 'uuidResolution' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    