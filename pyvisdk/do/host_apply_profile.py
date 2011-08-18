# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostApplyProfile(vim, *args, **kwargs):
    '''This DataObject has information about how a host should be configured.'''
    
    obj = vim.client.factory.create('ns0:HostApplyProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'policy', 'authentication', 'datetime', 'firewall', 'memory',
        'network', 'option', 'security', 'service', 'storage', 'userAccount',
        'usergroupAccount' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    