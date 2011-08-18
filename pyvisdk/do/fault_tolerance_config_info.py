# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FaultToleranceConfigInfo(vim, *args, **kwargs):
    '''FaultToleranceConfigInfo is a data object type containing Fault Tolerance
    settings for this virtual machine. role, instanceUuids and configPaths contain
    information about the whole fault tolerance group.'''
    
    obj = vim.client.factory.create('ns0:FaultToleranceConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configPaths', 'instanceUuids', 'role' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    