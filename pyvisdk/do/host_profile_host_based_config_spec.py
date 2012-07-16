
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostProfileHostBasedConfigSpec(vim, *args, **kwargs):
    '''The HostProfileHostBasedConfigSpec data object specifies the host from which
    configuration data is to be extracted and the profile(s) to be created or
    updated.'''
    
    obj = vim.client.factory.create('ns0:HostProfileHostBasedConfigSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'host' ]
    optional = [ 'useHostProfileEngine', 'annotation', 'enabled', 'name', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    