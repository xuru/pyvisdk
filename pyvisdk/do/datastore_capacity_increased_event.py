# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreCapacityIncreasedEvent(vim, *args, **kwargs):
    '''This event records when increase in a datastore's capacity is observed. It may
    happen due to different reasons, like extending or expanding a datastore.'''
    
    obj = vim.client.factory.create('ns0:DatastoreCapacityIncreasedEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'datastore', 'newCapacity', 'oldCapacity' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    