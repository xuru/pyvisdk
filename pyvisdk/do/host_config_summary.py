
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConfigSummary(vim, *args, **kwargs):
    '''An overview of the key configuration parameters.'''
    
    obj = vim.client.factory.create('ns0:HostConfigSummary')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'faultToleranceEnabled', 'name', 'port', 'vmotionEnabled' ]
    optional = [ 'agentVmDatastore', 'agentVmNetwork', 'featureVersion', 'product',
        'sslThumbprint', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    