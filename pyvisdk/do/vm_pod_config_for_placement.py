
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmPodConfigForPlacement(vim, *args, **kwargs):
    '''Initial VM configuration for the specified pod. This configuration will be
    saved to the pod config StorageDrsConfigInfo when the placement recommendations
    are applied.NOTE: This data object type and all of its methods are experimental
    and subject to change in future releases.'''
    
    obj = vim.client.factory.create('ns0:VmPodConfigForPlacement')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'storagePod' ]
    optional = [ 'disk', 'interVmRule', 'vmConfig', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    