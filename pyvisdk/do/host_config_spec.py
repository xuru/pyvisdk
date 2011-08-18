# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConfigSpec(vim, *args, **kwargs):
    '''The HostConfigSpec data object provides access to data objects that specify
    configuration changes to be applied to an ESX host.'''
    
    obj = vim.client.factory.create('ns0:HostConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeDirectory', 'datastorePrincipal', 'datastorePrincipalPasswd',
        'datetime', 'firewall', 'license', 'memory', 'nasDatastore', 'network',
        'nicTypeSelection', 'option', 'security', 'service', 'storageDevice',
        'userAccount', 'usergroupAccount' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    