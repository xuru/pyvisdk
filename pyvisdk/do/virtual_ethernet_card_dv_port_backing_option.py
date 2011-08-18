# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualEthernetCardDVPortBackingOption(vim, *args, **kwargs):
    '''This data object type contains the options for using a distributed virtual port
    virtual network card backing data object type.'''
    
    obj = vim.client.factory.create('ns0:VirtualEthernetCardDVPortBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    