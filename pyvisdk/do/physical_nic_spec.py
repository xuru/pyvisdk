# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNicSpec(vim, *args, **kwargs):
    '''This data object type describes the physical network adapter specification
    representing the properties on a physical network adapter that can be
    configured once the object exists.'''
    
    obj = vim.client.factory.create('ns0:PhysicalNicSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'ip', 'linkSpeed' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    