
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
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'cpuInfo', 'cpuPkg', 'memorySize', 'systemInfo' ]
    inherited = [ 'biosInfo', 'cpuFeature', 'cpuPowerManagementInfo', 'numaInfo', 'pciDevice' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    