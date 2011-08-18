# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ConfigTarget(vim, *args, **kwargs):
    '''The ConfigTarget class contains information about "physical" devices that can
    be used to back virtual devices.'''
    
    obj = vim.client.factory.create('ns0:ConfigTarget')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoVmotion', 'cdRom', 'datastore', 'distributedVirtualPortgroup',
        'distributedVirtualSwitch', 'floppy', 'ideDisk', 'legacyNetworkInfo',
        'maxMemMBOptimalPerf', 'network', 'numCpuCores', 'numCpus', 'numNumaNodes',
        'parallel', 'pciPassthrough', 'resourcePool', 'scsiDisk', 'scsiPassthrough',
        'serial', 'sound', 'usb' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    