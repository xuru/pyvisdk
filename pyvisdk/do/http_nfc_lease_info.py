
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HttpNfcLeaseInfo(vim, *args, **kwargs):
    '''This class holds information about the lease, such as the entity covered by the
    lease, and HTTP URLs for up/downloading file backings.'''
    
    obj = vim.client.factory.create('ns0:HttpNfcLeaseInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'entity', 'lease', 'leaseTimeout', 'totalDiskCapacityInKB' ]
    optional = [ 'deviceUrl', 'hostMap', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    