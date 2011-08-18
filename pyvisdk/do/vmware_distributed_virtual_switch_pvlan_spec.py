# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmwareDistributedVirtualSwitchPvlanSpec(vim, *args, **kwargs):
    '''This data type defines the configuration when PVLAN id is to be used for the
    ports.'''
    
    obj = vim.client.factory.create('ns0:VmwareDistributedVirtualSwitchPvlanSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'inherited', 'pvlanId' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    