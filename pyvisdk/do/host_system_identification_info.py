# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostSystemIdentificationInfo(vim, *args, **kwargs):
    '''This data object describes system identifying information of the host. This
    information may be vendor specific.'''
    
    obj = vim.client.factory.create('ns0:HostSystemIdentificationInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'identifierType', 'identifierValue' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    