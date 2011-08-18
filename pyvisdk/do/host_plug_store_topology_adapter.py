# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPlugStoreTopologyAdapter(vim, *args, **kwargs):
    '''This data object type is an association class that describes a host bus adapter
    and its associated storage Paths. The set of Paths on all the host bus adapters
    is the complete set of Paths in the system.'''
    
    obj = vim.client.factory.create('ns0:HostPlugStoreTopologyAdapter')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'adapter', 'key', 'path' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    