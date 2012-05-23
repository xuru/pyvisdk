
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ProductComponentInfo(vim, *args, **kwargs):
    '''ProductComponentInfo data object type describes installed components. Product
    component is defined as a software module that is released and versioned
    independently but has dependency relationship with other products. If one
    product, for usability or any other reason, bundles other products,
    ProductComponentInfo type may be used to describe installed components. For
    example, ESX product may bundle VI Client in its releases.'''
    
    obj = vim.client.factory.create('ns0:ProductComponentInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'id', 'name', 'release', 'version' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    