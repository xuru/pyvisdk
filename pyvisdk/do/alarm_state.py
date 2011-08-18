# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmState(vim, *args, **kwargs):
    '''Information about the alarm's state.'''
    
    obj = vim.client.factory.create('ns0:AlarmState')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'acknowledged', 'acknowledgedByUser', 'acknowledgedTime', 'alarm', 'entity',
        'key', 'overallStatus', 'time' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    