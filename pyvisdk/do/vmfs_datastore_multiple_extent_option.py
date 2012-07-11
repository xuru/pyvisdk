
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreMultipleExtentOption(vim, *args, **kwargs):
    '''Datastore addition policy to use multiple extents on the disk for a VMFS
    datastore. Multiple extents implies that more than one disk partition will be
    created on the disk for creating or increasing the capacity of a VMFS
    datastore. Multiple extents are needed when unpartitioned space is fragmented
    in the existing partition layout of the disk.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreMultipleExtentOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'vmfsExtent', 'layout' ]
    optional = [ 'partitionFormatChange', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    