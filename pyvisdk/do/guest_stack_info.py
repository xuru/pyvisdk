# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def GuestStackInfo(vim, *args, **kwargs):
    '''Information about the Internet Protocol stack as configured in the guest
    operating system.'''
    
    obj = vim.client.factory.create('ns0:GuestStackInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dhcpConfig', 'dnsConfig', 'ipRouteConfig', 'ipStackConfig' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    