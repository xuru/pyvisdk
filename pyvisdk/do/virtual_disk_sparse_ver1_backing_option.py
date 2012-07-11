
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskSparseVer1BackingOption(vim, *args, **kwargs):
    '''This data object type contains the available options when backing a virtual
    disk using a host file with the sparse file format from GSX Server 2.x.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskSparseVer1BackingOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'diskModes', 'growable', 'split', 'writeThrough', 'type' ]
    optional = [ 'fileNameExtensions', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    