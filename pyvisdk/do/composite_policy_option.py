
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CompositePolicyOption(vim, *args, **kwargs):
    '''DataObject represents a composite Policy that is created by the user using
    different PolicyOptions. The options set in the CompositePolicyOption should be
    derived from the possible options as indicated by the
    CompositePolicyOptionMetadata.'''
    
    obj = vim.client.factory.create('ns0:CompositePolicyOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'id' ]
    optional = [ 'option', 'parameter', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    