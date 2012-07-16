
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def IscsiDependencyEntity(vim, *args, **kwargs):
    '''Defines a dependency entity. Contains the affected Virtual NIC device name and
    iSCSI HBA name (if Virtual NIC is associated with the HBA). See
    IscsiMigrationDependency'''
    
    obj = vim.client.factory.create('ns0:IscsiDependencyEntity')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'pnicDevice', 'vmhbaName', 'vnicDevice' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    