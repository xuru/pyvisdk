# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmInfo(vim, *args, **kwargs):
    '''Attributes of an alarm.'''
    
    obj = vim.client.factory.create('ns0:AlarmInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'action', 'actionFrequency', 'description', 'enabled', 'expression', 'name',
        'setting', 'alarm', 'creationEventId', 'entity', 'key', 'lastModifiedTime',
        'lastModifiedUser' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    