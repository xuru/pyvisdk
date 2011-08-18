# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostProfileManagerConfigTaskList(vim, *args, **kwargs):
    '''DataObject which represents list of tasks that will be performed on the host
    during application of a HostProfile.'''
    
    obj = vim.client.factory.create('ns0:HostProfileManagerConfigTaskList')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configSpec', 'taskDescription' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    