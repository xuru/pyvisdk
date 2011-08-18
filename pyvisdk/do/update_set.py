# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def UpdateSet(vim, *args, **kwargs):
    '''A set of updates that represent the changes since a prior call to
    CheckForUpdates, WaitForUpdates, or WaitForUpdatesEx.'''
    
    obj = vim.client.factory.create('ns0:UpdateSet')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'filterSet', 'truncated', 'version' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    