
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def SelectionSpec(vim, *args, **kwargs):
    '''The SelectionSpec is the base type for data object types that specify what
    additional objects to filter. The base type contains only an optional "name"
    field, which allows a selection to be named for future reference. More
    information is available in the subtype.Named selections support recursive
    specifications on an object hierarchy. When used by a derived object, the
    "name" field allows other SelectionSpec objects to refer to the object by name.
    When used as the base type only, the "name" field indicates recursion to the
    derived object by name.Names are meaningful only within the same FilterSpec.'''
    
    obj = vim.client.factory.create('ns0:SelectionSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'name', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    