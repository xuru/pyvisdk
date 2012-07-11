
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskSparseVer2BackingOption(vim, *args, **kwargs):
    '''This data object type contains the options available when backing a virtual
    disk using a host file with the sparse file format from VMware Server.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskSparseVer2BackingOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'diskMode', 'growable', 'hotGrowable', 'split', 'uuid', 'writeThrough', 'type' ]
    optional = [ 'fileNameExtensions', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    