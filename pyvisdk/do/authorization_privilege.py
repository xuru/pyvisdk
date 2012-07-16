
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AuthorizationPrivilege(vim, *args, **kwargs):
    '''This data object type provides access to some aspect of the system. Privileges
    are generally independent. This means a user with a privilege usually can
    perform an associated set of actions without needing any additional supporting
    privileges.Within each product version, privileges do not change. See
    AuthorizationDescription for detailed information on the privileges defined by
    the system.'''
    
    obj = vim.client.factory.create('ns0:AuthorizationPrivilege')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'name', 'onParent', 'privGroupName', 'privId' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    