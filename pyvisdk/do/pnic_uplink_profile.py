
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PnicUplinkProfile(vim, *args, **kwargs):
    '''The PnicUplinkProfile data object specifies the mapping between a physical NIC
    and an uplink port. The policy property contains the configuration data values.'''
    
    obj = vim.client.factory.create('ns0:PnicUplinkProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'key', 'enabled' ]
    optional = [ 'policy', 'profileTypeName', 'profileVersion', 'property', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    