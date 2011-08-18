# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AutoStartDefaults(vim, *args, **kwargs):
    '''Defines the system default auto-start/auto-stop values.'''
    
    obj = vim.client.factory.create('ns0:AutoStartDefaults')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'startDelay', 'stopAction', 'stopDelay', 'waitForHeartbeat' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    