
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasHostRecommendation(vim, *args, **kwargs):
    '''A host recommendation for a virtual machine managed by the VMware HA Service.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasHostRecommendation')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'host' ]
    optional = [ 'drsRating', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    