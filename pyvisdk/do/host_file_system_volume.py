
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFileSystemVolume(vim, *args, **kwargs):
    '''Detailed information about a file system. This is a base type for derived types
    that have more specific details about specific filesystem types.Typically a
    FileSystem is exposed as a datatoreSee DatastoreInfoSee HostVmfsVolumeSee
    HostNasVolumeSee HostLocalFileSystemVolumeSee HostVfatVolume'''
    
    obj = vim.client.factory.create('ns0:HostFileSystemVolume')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'capacity', 'name', 'type' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    