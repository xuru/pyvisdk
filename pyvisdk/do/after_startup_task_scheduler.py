# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AfterStartupTaskScheduler(vim, *args, **kwargs):
    '''The AfterStartupTaskScheduler data object establishes the time that a scheduled
    task will run after the vCenter server restarts.'''
    
    obj = vim.client.factory.create('ns0:AfterStartupTaskScheduler')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeTime', 'expireTime', 'minute' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    