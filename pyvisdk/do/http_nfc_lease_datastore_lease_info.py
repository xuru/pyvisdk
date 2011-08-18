# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HttpNfcLeaseDatastoreLeaseInfo(vim, *args, **kwargs):
    '''For a given datastore, represented by datastoreKey, contains a list of leased
    multi-POST-capable hosts connected to it.'''
    
    obj = vim.client.factory.create('ns0:HttpNfcLeaseDatastoreLeaseInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastoreKey', 'hosts' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    