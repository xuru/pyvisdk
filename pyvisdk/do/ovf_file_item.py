
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfFileItem(vim, *args, **kwargs):
    '''An FileItem represents a file that must be uploaded by the caller when the
    inventory objects has been created in VI. These objects are created by
    ResourcePool.importVApp.Files can either be new files, in which case the
    "create" flag will be true, or updates to existing files in VI. The latter is
    used to support the OVF parentRef mechanism for Disks.'''
    
    obj = vim.client.factory.create('ns0:OvfFileItem')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'cimType', 'create', 'deviceId', 'path' ]
    optional = [ 'chunkSize', 'compressionMethod', 'size', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    