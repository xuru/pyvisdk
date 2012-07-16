
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNicCdpDeviceCapability(vim, *args, **kwargs):
    '''The capability of the CDP-awared device that connects to a Physical NIC.
    PhysicalNicCdpInfo'''
    
    obj = vim.client.factory.create('ns0:PhysicalNicCdpDeviceCapability')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'host', 'igmpEnabled', 'networkSwitch', 'repeater', 'router',
        'sourceRouteBridge', 'transparentBridge' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    