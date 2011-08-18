# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSwitchSelectionProfile(vim, *args, **kwargs):
    '''This data object type represents the profile for choosing the virtual switch
    that is connected to a port group.'''
    
    obj = vim.client.factory.create('ns0:VirtualSwitchSelectionProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'policy' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    