
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreOption(vim, *args, **kwargs):
    '''VMFS datastore provisioning option that can be applied on a disk. VMFS
    datastores can be created or have their capacity increased using storage from a
    disk. There are often multiple ways in which extents can be allocated on a
    disk. Each instance of this structure represents one of the possible options
    that can be applied to provisiong VMFS datastore storage. Only options that
    follow ESX Server best practice guidelines will be presented.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'info', 'spec' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    