
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConfigManager(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:HostConfigManager')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'advancedOption', 'authenticationManager', 'autoStartManager',
        'bootDeviceSystem', 'cpuScheduler', 'datastoreSystem', 'dateTimeSystem',
        'diagnosticSystem', 'firewallSystem', 'firmwareSystem', 'healthStatusSystem',
        'kernelModuleSystem', 'licenseManager', 'memoryManager', 'networkSystem',
        'patchManager', 'pciPassthruSystem', 'powerSystem', 'serviceSystem',
        'snmpSystem', 'storageSystem', 'virtualNicManager', 'vmotionSystem' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    