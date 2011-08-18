# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventFilterSpec(vim, *args, **kwargs):
    '''Event filter used to query events in the history collector database. The client
    creates an event history collector with a filter specification, then retrieves
    the events from the event history collector.'''
    
    obj = vim.client.factory.create('ns0:EventFilterSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'alarm', 'category', 'disableFullMessage', 'entity', 'eventChainId',
        'eventTypeId', 'scheduledTask', 'tag', 'time', 'type', 'userName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    