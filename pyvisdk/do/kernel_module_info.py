# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def KernelModuleInfo(vim, *args, **kwargs):
    '''Information about a kernel module.'''
    
    obj = vim.client.factory.create('ns0:KernelModuleInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 13:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bssSection', 'dataSection', 'enabled', 'filename', 'id', 'loaded', 'name',
        'optionString', 'readOnlySection', 'textSection', 'useCount', 'version',
        'writableSection' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    