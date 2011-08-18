# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def Extension(vim, *args, **kwargs):
    '''This data object type contains all information about an extension. An extension
    may contain zero or more server interfaces and zero or more clients.'''
    
    obj = vim.client.factory.create('ns0:Extension')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'client', 'company', 'description', 'eventList', 'faultList', 'healthInfo',
        'key', 'lastHeartbeatTime', 'privilegeList', 'resourceList', 'server',
        'subjectName', 'taskList', 'type', 'version' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    