
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVmfsSpec(vim, *args, **kwargs):
    '''This data object type describes the VMware File System (VMFS) creation
    specification. Once created, these properties for the most part cannot be
    changed. There are a few exceptions.'''
    
    obj = vim.client.factory.create('ns0:HostVmfsSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'extent', 'majorVersion', 'volumeName' ]
    optional = [ 'blockSizeMb', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    