
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNasVolumeSpec(vim, *args, **kwargs):
    '''Specification for creating NAS volume.When mounting a NAS volume on multiple
    hosts, the same remoteHost and remotePath values should be used on every host,
    otherwise it will be treated as different datastores. For example, if one host
    references the remotePath of a NAS volume as "/mnt/mount1" and another
    references it as "/mnt/mount1/", it will not be recognized as the same
    datastore.'''
    
    obj = vim.client.factory.create('ns0:HostNasVolumeSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'accessMode', 'localPath', 'remoteHost', 'remotePath' ]
    optional = [ 'password', 'type', 'userName', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    