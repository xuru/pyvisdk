# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineRuntimeInfo(vim, *args, **kwargs):
    '''The RuntimeInfo data object type provides information about the execution state
    and history of a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineRuntimeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bootTime', 'cleanPowerOff', 'connectionState', 'device',
        'faultToleranceState', 'host', 'maxCpuUsage', 'maxMemoryUsage',
        'memoryOverhead', 'minRequiredEVCModeKey', 'needSecondaryReason',
        'numMksConnections', 'powerState', 'question', 'recordReplayState',
        'suspendInterval', 'suspendTime', 'toolsInstallerMounted' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    