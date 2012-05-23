
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StorageDrsConfigSpec(vim, *args, **kwargs):
    '''The StorageDrsConfigSpec data object provides a set of update specifications
    for storage DRS configuration. To support incremental changes, these properties
    are all optional.NOTE: This data object type and all of its methods are
    experimental and subject to change in future releases.'''
    
    obj = vim.client.factory.create('ns0:StorageDrsConfigSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'podConfigSpec', 'vmConfigSpec', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    