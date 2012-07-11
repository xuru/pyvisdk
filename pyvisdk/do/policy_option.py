
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PolicyOption(vim, *args, **kwargs):
    '''The PolicyOption data object represents one or more configuration values. A
    policy option is one of the configuration options from the
    ProfilePolicyMetadata.possibleOption list.'''
    
    obj = vim.client.factory.create('ns0:PolicyOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'id' ]
    optional = [ 'parameter', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    