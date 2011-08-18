# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventAlarmExpression(vim, *args, **kwargs):
    '''An alarm expression that uses the event stream to trigger the alarm.This alarm
    is triggered when an event matching this expression gets logged.'''
    
    obj = vim.client.factory.create('ns0:EventAlarmExpression')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'comparisons', 'eventType', 'eventTypeId', 'objectType', 'status' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    