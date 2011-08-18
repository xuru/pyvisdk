# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNatServiceSpec(vim, *args, **kwargs):
    '''This data object type provides the details about the Network Address
    Translation (NAT) service.'''
    
    obj = vim.client.factory.create('ns0:HostNatServiceSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeFtp', 'allowAnyOui', 'configPort', 'ipGatewayAddress', 'nameService',
        'portForward', 'udpTimeout', 'virtualSwitch' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    