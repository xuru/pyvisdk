# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def RecurrentTaskScheduler(vim, *args, **kwargs):
    '''The RecurrentTaskScheduler data object is the base type for the hierarchy that
    includes hourly, daily, weekly, and monthly task schedulers.'''
    
    obj = vim.client.factory.create('ns0:RecurrentTaskScheduler')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeTime', 'expireTime', 'interval' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    