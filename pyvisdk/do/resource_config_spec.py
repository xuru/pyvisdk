
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourceConfigSpec(vim, *args, **kwargs):
    '''This data object type is a specification for a set of resources allocated to a
    virtual machine or a resource pool.'''
    
    obj = vim.client.factory.create('ns0:ResourceConfigSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'cpuAllocation', 'memoryAllocation' ]
    optional = [ 'changeVersion', 'entity', 'lastModified', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    