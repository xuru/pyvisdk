
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourcePoolResourceUsage(vim, *args, **kwargs):
    '''Specifies the resource usage for either memory or CPU. For CPU the unit is MHz,
    for memory the unit is bytes.In the typical case, where a resourcepool is in a
    consistent state, unreservedForVm will be equal to unreservedForPool. Hence, we
    can simply say talk about unreserved resources.If the reservation on the
    resource pool is not expandable, then the following is true:If the reservation
    on the resource pool is expandable, then the following is true:'''
    
    obj = vim.client.factory.create('ns0:ResourcePoolResourceUsage')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'maxUsage', 'overallUsage', 'reservationUsed', 'reservationUsedForVm',
        'unreservedForPool', 'unreservedForVm' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    