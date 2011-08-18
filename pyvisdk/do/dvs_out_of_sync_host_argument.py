# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DvsOutOfSyncHostArgument(vim, *args, **kwargs):
    '''The host on which the DVS configuration is different from that of Virtual
    Center server.'''
    
    obj = vim.client.factory.create('ns0:DvsOutOfSyncHostArgument')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configParamters', 'outOfSyncHost' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    