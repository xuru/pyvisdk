# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostSslThumbprintInfo(vim, *args, **kwargs):
    '''The SSL thumbprint information for a host to login into other hosts in the same
    cluster without username/password authentication.'''
    
    obj = vim.client.factory.create('ns0:HostSslThumbprintInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'principal', 'sslThumbprints' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    