# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConnectInfo(vim, *args, **kwargs):
    '''This data object type contains information about a single host that can be used
    by the connection wizard. This can be returned without adding the host to
    VirtualCenter.'''
    
    obj = vim.client.factory.create('ns0:HostConnectInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'clusterSupported', 'datastore', 'host', 'license', 'network', 'serverIp',
        'vimAccountNameRequired', 'vm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    