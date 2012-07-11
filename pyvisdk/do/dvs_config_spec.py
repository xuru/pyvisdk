
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSConfigSpec(vim, *args, **kwargs):
    '''Specification to reconfigure a DistributedVirtualSwitch.'''
    
    obj = vim.client.factory.create('ns0:DVSConfigSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'configVersion', 'contact', 'defaultPortConfig', 'description', 'extensionKey',
        'host', 'maxPorts', 'name', 'numStandalonePorts', 'policy', 'switchIpAddress',
        'uplinkPortgroup', 'uplinkPortPolicy', 'vendorSpecificConfig',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    