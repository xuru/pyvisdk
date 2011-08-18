# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPlugStoreTopologyPath(vim, *args, **kwargs):
    '''This data object type is an association class that describes a Path and its
    associated Device. A Path may be claimed by at most one Device.'''
    
    obj = vim.client.factory.create('ns0:HostPlugStoreTopologyPath')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'adapter', 'channelNumber', 'device', 'key', 'lunNumber', 'name', 'target',
        'targetNumber' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    