
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TraversalSpec(vim, *args, **kwargs):
    '''The TraversalSpec data object type specifies how to derive a new set of objects
    to add to the filter.It specifies a property path whose value is either another
    managed object or an array of managed objects included in the set of objects
    for consideration. This data object can also be named, using the "name" field
    in the base type.'''
    
    obj = vim.client.factory.create('ns0:TraversalSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'path', 'type' ]
    optional = [ 'selectSet', 'skip', 'name', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    