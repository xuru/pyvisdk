
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AuthenticationProfile(vim, *args, **kwargs):
    '''The AuthenticationProfile data object represents the host configuration for
    authentication. If a profile plug-in defines policies or subprofiles, use the
    policy or property list to access the additional configuration data.'''
    
    obj = vim.client.factory.create('ns0:AuthenticationProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'enabled' ]
    optional = [ 'activeDirectory', 'policy', 'profileTypeName', 'profileVersion', 'property',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    