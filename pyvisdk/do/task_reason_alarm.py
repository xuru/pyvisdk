# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TaskReasonAlarm(vim, *args, **kwargs):
    '''Indicates that the task was queued by an alarm.'''
    
    obj = vim.client.factory.create('ns0:TaskReasonAlarm')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'alarm', 'alarmName', 'entity', 'entityName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    