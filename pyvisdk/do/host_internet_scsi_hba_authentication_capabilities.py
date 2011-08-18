# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaAuthenticationCapabilities(vim, *args, **kwargs):
    '''The authentication capabilities for this host bus adapter.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaAuthenticationCapabilities')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chapAuthSettable', 'krb5AuthSettable', 'mutualChapSettable',
        'spkmAuthSettable', 'srpAuthSettable', 'targetChapSettable',
        'targetMutualChapSettable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    