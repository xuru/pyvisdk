
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PropertyFilterUpdate(vim, *args, **kwargs):
    '''The PropertyFilterUpdate data object type contains a list of updates to data
    visible through a specific filter. Note that if a property changes through
    multiple filters, then a client receives an update for each filter.'''
    
    obj = vim.client.factory.create('ns0:PropertyFilterUpdate')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'filter' ]
    optional = [ 'missingSet', 'objectSet', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    