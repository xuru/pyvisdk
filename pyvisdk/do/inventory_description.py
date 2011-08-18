# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def InventoryDescription(vim, *args, **kwargs):
    '''Data object to capture all information needed to describe a sample inventory.'''
    
    obj = vim.client.factory.create('ns0:InventoryDescription')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'numClusters', 'numCpuDev', 'numDiskDev', 'numHosts', 'numNetDev',
        'numResourcePools', 'numvCpuDev', 'numvDiskDev', 'numVirtualMachines',
        'numvNetDev' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    