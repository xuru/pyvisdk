
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHardwareInfo(vim, *args, **kwargs):
    '''The HardwareInfo data object type describes the hardware configuration of the
    host.'''
    
    obj = vim.client.factory.create('ns0:HostHardwareInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'cpuInfo', 'cpuPkg', 'memorySize', 'smcPresent', 'systemInfo' ]
    optional = [ 'biosInfo', 'cpuFeature', 'cpuPowerManagementInfo', 'numaInfo', 'pciDevice',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    