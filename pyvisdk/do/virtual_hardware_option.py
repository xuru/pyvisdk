# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualHardwareOption(vim, *args, **kwargs):
    '''The VirtualHardwareOption data object contains the options available for all
    virtual devices.'''
    
    obj = vim.client.factory.create('ns0:VirtualHardwareOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceListReadonly', 'hwVersion', 'licensingLimit', 'memoryMB', 'numCPU',
        'numCpuReadonly', 'numIDEControllers', 'numPCIControllers',
        'numPS2Controllers', 'numSIOControllers', 'numSupportedWwnNodes',
        'numSupportedWwnPorts', 'numUSBControllers', 'resourceConfigOption',
        'virtualDeviceOption' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    