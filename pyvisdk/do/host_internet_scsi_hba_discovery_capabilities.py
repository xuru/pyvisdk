
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaDiscoveryCapabilities(vim, *args, **kwargs):
    '''The discovery capabilities for this host bus adapter. At least one discovery
    mode must always be active. Multiple modes may be active at the same time.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaDiscoveryCapabilities')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'iSnsDiscoverySettable', 'sendTargetsDiscoverySettable',
        'slpDiscoverySettable', 'staticTargetDiscoverySettable' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    