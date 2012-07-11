
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostForceMountedInfo(vim, *args, **kwargs):
    '''When the system detects a copy of a VmfsVolume, it will not be auto-mounted on
    the host and it will be detected as 'UnresolvedVmfsVolume'. If user decides to
    keep the original Uuid and mount it on the host, it will have 'forceMounted'
    flag and 'forceMountedInfo' set. 'ForceMountedInfo' provides additional
    information specific to user-mounted VmfsVolume.'''
    
    obj = vim.client.factory.create('ns0:HostForceMountedInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'mounted', 'persist' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    