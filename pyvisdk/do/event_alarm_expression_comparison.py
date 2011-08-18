# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventAlarmExpressionComparison(vim, *args, **kwargs):
    '''Encapsulates Comparison of an event's attribute to a value.'''
    
    obj = vim.client.factory.create('ns0:EventAlarmExpressionComparison')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'attributeName', 'operator', 'value' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    