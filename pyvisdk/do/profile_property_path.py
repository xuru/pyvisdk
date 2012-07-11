
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ProfilePropertyPath(vim, *args, **kwargs):
    '''The ProfilePropertyPath data object represents the path to either a profile or
    a policy option. If both and are specified, the combination of the two
    identifies a specific profile policy option.'''
    
    obj = vim.client.factory.create('ns0:ProfilePropertyPath')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'profilePath' ]
    optional = [ 'policyId', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    