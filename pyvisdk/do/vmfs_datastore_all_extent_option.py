
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreAllExtentOption(vim, *args, **kwargs):
    '''Datastore addition policy to use the entire disk as a single extent for a VMFS
    datastore. If there is any data on the disk, it will be overwritten.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreAllExtentOption')

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
    