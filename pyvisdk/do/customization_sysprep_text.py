# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationSysprepText(vim, *args, **kwargs):
    '''An alternate way to specify the answer file. This string is more or less
    written exactly to the answer file on the target virtual disk.'''
    
    obj = vim.client.factory.create('ns0:CustomizationSysprepText')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'value' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    