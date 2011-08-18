# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDnsConfigSpec(vim, *args, **kwargs):
    '''Dataobject for configuring the DNS settings on the host.'''
    
    obj = vim.client.factory.create('ns0:HostDnsConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'address', 'dhcp', 'domainName', 'hostName', 'searchDomain',
        'virtualNicDevice', 'virtualNicConnection' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    