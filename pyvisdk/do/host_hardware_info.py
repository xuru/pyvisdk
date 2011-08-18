# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHardwareInfo(vim, *args, **kwargs):
    '''The HardwareInfo data object type describes the hardware configuration of the
    host.'''
    
    obj = vim.client.factory.create('ns0:HostHardwareInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'biosInfo', 'cpuFeature', 'cpuInfo', 'cpuPkg', 'cpuPowerManagementInfo',
        'memorySize', 'numaInfo', 'pciDevice', 'systemInfo' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    