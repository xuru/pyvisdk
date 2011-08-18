# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigOptionDescriptor(vim, *args, **kwargs):
    '''Contains the definition of a unique key that can be used to retrieve a
    configOption object.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigOptionDescriptor')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'createSupported', 'defaultConfigOption', 'description', 'host', 'key' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    