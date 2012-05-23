
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PropertySpec(vim, *args, **kwargs):
    '''Within a PropertyFilterSpec, A PropertySpec specifies which properties should
    be reported to the client for objects of the given managed object type that are
    visited and not skipped. One more subtle side effect is that if a managed
    object is visited and not skipped, but there is no PropertySpec associated with
    the managed object's type, the managed object will not be reported to the
    client.Also, the set of properties applicable to a given managed object type is
    the union of the properties implied by the PropertySpec objects even, in the
    case of a RetrieveResult, where there may be an applicable PropertySpec in more
    than one filter.'''
    
    obj = vim.client.factory.create('ns0:PropertySpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'type' ]
    optional = [ 'all', 'pathSet', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    