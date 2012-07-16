
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def Permission(vim, *args, **kwargs):
    '''This data object type provides assignment of some role access to a principal on
    a specific entity. A ManagedEntity is limited to one permission per principal.'''
    
    obj = vim.client.factory.create('ns0:Permission')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'group', 'principal', 'propagate', 'roleId' ]
    optional = [ 'entity', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    