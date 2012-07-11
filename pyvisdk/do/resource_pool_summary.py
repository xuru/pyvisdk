
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourcePoolSummary(vim, *args, **kwargs):
    '''This data object type encapsulates a typical set of resource pool information
    that is useful for list views and summary pages.'''
    
    obj = vim.client.factory.create('ns0:ResourcePoolSummary')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'config', 'name', 'runtime' ]
    optional = [ 'configuredMemoryMB', 'quickStats', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    