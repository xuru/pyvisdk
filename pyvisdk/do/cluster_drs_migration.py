# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDrsMigration(vim, *args, **kwargs):
    '''Describes a single virtual machine migration.'''
    
    obj = vim.client.factory.create('ns0:ClusterDrsMigration')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cpuLoad', 'destination', 'destinationCpuLoad', 'destinationMemoryLoad', 'key',
        'memoryLoad', 'source', 'sourceCpuLoad', 'sourceMemoryLoad', 'time', 'vm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    