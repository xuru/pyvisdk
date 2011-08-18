# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdromRemoteAtapiBackingOption(vim, *args, **kwargs):
    '''The VirtualCdromOption.RemoteAtapiBackingOption data object type contains the
    options for the remote ATAPI CD-ROM device backing. Note that the server cannot
    present a list of valid remote backing devices because it is unable to scan
    remote hosts.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdromRemoteAtapiBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    