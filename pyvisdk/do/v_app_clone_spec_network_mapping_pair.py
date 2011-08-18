# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppCloneSpecNetworkMappingPair(vim, *args, **kwargs):
    '''Maps one network to another as part of the clone process.Instances of this
    class are used in the field networkMapping'''
    
    obj = vim.client.factory.create('ns0:VAppCloneSpecNetworkMappingPair')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'destination', 'source' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    