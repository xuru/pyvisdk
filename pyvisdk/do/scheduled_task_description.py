# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ScheduledTaskDescription(vim, *args, **kwargs):
    '''Static strings for scheduled tasks. These strings are locale-specific.'''
    
    obj = vim.client.factory.create('ns0:ScheduledTaskDescription')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'action', 'dayOfWeek', 'schedulerInfo', 'state', 'weekOfMonth' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    