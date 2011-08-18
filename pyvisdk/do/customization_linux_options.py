# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationLinuxOptions(vim, *args, **kwargs):
    '''Base object type for optional operations supported by the customization process
    for Linux.'''
    
    obj = vim.client.factory.create('ns0:CustomizationLinuxOptions')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [  ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    