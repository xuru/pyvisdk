
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSNetworkResourceManagementCapability(vim, *args, **kwargs):
    '''Dataobject representing the feature capabilities of network resource management
    supported by the vSphere Distributed Switch.'''
    
    obj = vim.client.factory.create('ns0:DVSNetworkResourceManagementCapability')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'networkResourceManagementSupported', 'networkResourcePoolHighShareValue',
        'qosSupported', 'userDefinedNetworkResourcePoolsSupported' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    