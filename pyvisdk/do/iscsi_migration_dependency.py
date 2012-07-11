
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def IscsiMigrationDependency(vim, *args, **kwargs):
    '''Provides migration dependency information for a given Physical NIC. Lists all
    the iSCSI and networking resources impacted if migration of a given Physical
    NIC is to take place.'''
    
    obj = vim.client.factory.create('ns0:IscsiMigrationDependency')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'migrationAllowed' ]
    optional = [ 'dependency', 'disallowReason', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    