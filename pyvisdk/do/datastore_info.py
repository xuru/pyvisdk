
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreInfo(vim, *args, **kwargs):
    '''Detailed information about a datastore. This is a base type for derived types
    that have more specific details about a datastore.See HostVmfsVolumeSee
    HostNasVolumeSee HostLocalFileSystemVolume'''
    
    obj = vim.client.factory.create('ns0:DatastoreInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'freeSpace', 'maxFileSize', 'name', 'url' ]
    optional = [ 'timestamp', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    