# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineAffinityInfo(vim, *args, **kwargs):
    '''Specification of scheduling affinity.Scheduling affinity is used for explicitly
    specifying which processors or NUMA nodes may be used by a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineAffinityInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'affinitySet' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    