# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'advancedOption', 'authenticationManager', 'autoStartManager',
        'bootDeviceSystem', 'cpuScheduler', 'datastoreSystem', 'dateTimeSystem',
        'diagnosticSystem', 'firewallSystem', 'firmwareSystem', 'healthStatusSystem',
        'kernelModuleSystem', 'licenseManager', 'memoryManager', 'networkSystem',
        'patchManager', 'pciPassthruSystem', 'powerSystem', 'serviceSystem',
        'snmpSystem', 'storageSystem', 'virtualNicManager', 'vmotionSystem' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    