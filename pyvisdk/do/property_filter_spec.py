
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PropertyFilterSpec(vim, *args, **kwargs):
    '''Specify the property data that is included in a filter. A filter can specify
    part of a single managed object, or parts of multiple related managed objects
    in an inventory hierarchy - for example, to collect updates from all virtual
    machines in a given folder.'''
    
    obj = vim.client.factory.create('ns0:PropertyFilterSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'objectSet', 'propSet' ]
    optional = [ 'reportMissingObjectsInResults', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    