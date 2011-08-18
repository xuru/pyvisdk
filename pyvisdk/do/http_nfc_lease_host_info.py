# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HttpNfcLeaseHostInfo(vim, *args, **kwargs):
    '''Contains information about how to connect to a given host.'''
    
    obj = vim.client.factory.create('ns0:HttpNfcLeaseHostInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'sslThumbprint', 'url' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    