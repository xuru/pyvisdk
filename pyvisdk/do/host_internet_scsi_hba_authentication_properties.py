# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaAuthenticationProperties(vim, *args, **kwargs):
    '''The authentication settings for this host bus adapter or target.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaAuthenticationProperties')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chapAuthEnabled', 'chapAuthenticationType', 'chapInherited', 'chapName',
        'chapSecret', 'mutualChapAuthenticationType', 'mutualChapInherited',
        'mutualChapName', 'mutualChapSecret' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    