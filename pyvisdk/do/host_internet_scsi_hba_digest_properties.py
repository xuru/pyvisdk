# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaDigestProperties(vim, *args, **kwargs):
    '''The digest settings for this host bus adapter.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaDigestProperties')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dataDigestInherited', 'dataDigestType', 'headerDigestInherited',
        'headerDigestType' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    