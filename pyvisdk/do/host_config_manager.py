
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConfigManager(vim, *args, **kwargs):
    '''This data object type describes the configuration of a host across products and
    versions.'''
    
    obj = vim.client.factory.create('ns0:HostConfigManager')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'advancedOption', 'authenticationManager', 'autoStartManager',
        'bootDeviceSystem', 'cacheConfigurationManager', 'cpuScheduler',
        'datastoreSystem', 'dateTimeSystem', 'diagnosticSystem', 'esxAgentHostManager',
        'firewallSystem', 'firmwareSystem', 'healthStatusSystem', 'imageConfigManager',
        'iscsiManager', 'kernelModuleSystem', 'licenseManager', 'memoryManager',
        'networkSystem', 'patchManager', 'pciPassthruSystem', 'powerSystem',
        'serviceSystem', 'snmpSystem', 'storageSystem', 'virtualNicManager',
        'vmotionSystem', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    