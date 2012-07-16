
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DynamicData(vim, *args, **kwargs):
    '''DynamicData is a builtin object model data object type for manipulating data
    properties dynamically. The primary usage is as a base class for types that may
    be extended with subtypes in the future, where new properties should be sent to
    old clients as a set of dynamic properties.'''
    
    obj = vim.client.factory.create('ns0:DynamicData')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    