# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineRelocateSpec(vim, *args, **kwargs):
    '''Specification for moving or copying a virtual machine to a different datastore
    or host.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineRelocateSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastore', 'disk', 'diskMoveType', 'host', 'pool', 'transform' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    