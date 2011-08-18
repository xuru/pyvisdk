# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNumaNode(vim, *args, **kwargs):
    '''Information about a single NUMA node.NOTE: This data object is not modeled
    correctly if the NUMA node contains multiple disjoint memory ranges. If there
    are multiple memory ranges, the client will see one memory ranges from this
    NumaNode object, and the memory range may or may not belong to this NUMA node.'''
    
    obj = vim.client.factory.create('ns0:HostNumaNode')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cpuID', 'memoryRangeBegin', 'memoryRangeLength', 'typeId' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    