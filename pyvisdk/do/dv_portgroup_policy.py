
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVPortgroupPolicy(vim, *args, **kwargs):
    '''The DistributedVirtualPortgroup policies. This field is not applicable when
    queried directly against an ESX host.'''
    
    obj = vim.client.factory.create('ns0:DVPortgroupPolicy')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'blockOverrideAllowed', 'livePortMovingAllowed', 'portConfigResetAtDisconnect',
        'shapingOverrideAllowed', 'vendorConfigOverrideAllowed' ]
    optional = [ 'networkResourcePoolOverrideAllowed', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    