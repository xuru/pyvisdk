# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineCloneSpec(vim, *args, **kwargs):
    '''Specification for a virtual machine cloning operation.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineCloneSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'config', 'customization', 'location', 'powerOn', 'snapshot', 'template' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    