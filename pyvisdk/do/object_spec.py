
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ObjectSpec(vim, *args, **kwargs):
    '''Within a PropertyFilterSpec, the ObjectSpec data object type specifies the
    managed object at which the filter begins to collect the managed object
    references and properties specified by the associated PropertySpec set. If the
    "skip" property is present and set to true, then the filter does not check to
    see if the starting object's type matches any of the types listed in the
    associated sets of PropertySpec data objects.If the selectSet property is
    present, then this specifies additional objects to filter. These objects are
    defined by one or more SelectionSpec objects.'''
    
    obj = vim.client.factory.create('ns0:ObjectSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'obj' ]
    optional = [ 'selectSet', 'skip', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    