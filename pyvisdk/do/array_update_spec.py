
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ArrayUpdateSpec(vim, *args, **kwargs):
    '''An ArrayUpdateSpec data object type is a common superclass for supporting
    incremental updates to arrays.The common code pattern is:The ArrayUpdateSpec
    contains the following:* : the type of operation being performed. * : In the
    case of a remove operation, the key value that identifies the array to be
    removed.'''
    
    obj = vim.client.factory.create('ns0:ArrayUpdateSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'operation' ]
    optional = [ 'removeKey', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    