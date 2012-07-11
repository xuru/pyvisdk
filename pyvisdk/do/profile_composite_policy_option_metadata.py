
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ProfileCompositePolicyOptionMetadata(vim, *args, **kwargs):
    '''The ProfileCompositePolicyOptionMetadata data object represents the metadata
    information for a composite PolicyOption. The user will retrieve metadata
    information about a composite policy and then combine policy options to produce
    the composite policy option.'''
    
    obj = vim.client.factory.create('ns0:ProfileCompositePolicyOptionMetadata')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'option', 'id' ]
    optional = [ 'parameter', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    