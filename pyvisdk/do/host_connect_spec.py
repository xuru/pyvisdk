# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConnectSpec(vim, *args, **kwargs):
    '''Specifies the parameters needed to add a single host. This includes a small set
    of optional information about the host configuration. This allows the network
    and datastore configuration of the host to be synchronized with the naming
    conventions of the datacenter, as well as the configuration of a vim account
    (the username/password for the virtual machine files that is created on disk).'''
    
    obj = vim.client.factory.create('ns0:HostConnectSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'force', 'hostName', 'managementIp', 'password', 'port', 'sslThumbprint',
        'userName', 'vimAccountName', 'vimAccountPassword', 'vmFolder' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    