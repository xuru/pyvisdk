
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreCreateSpec(vim, *args, **kwargs):
    '''This data object type is used when creating a new VMFS datastore, to create a
    specification for the VMFS datastore.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreCreateSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'partition', 'vmfs', 'diskUuid' ]
    optional = [ 'extent', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    