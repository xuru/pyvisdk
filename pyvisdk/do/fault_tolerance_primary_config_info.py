# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FaultTolerancePrimaryConfigInfo(vim, *args, **kwargs):
    '''FaultTolerancePrimaryConfigInfo is a data object type containing Fault
    Tolerance settings for a primary virtual machine in a fault tolerance group'''
    
    obj = vim.client.factory.create('ns0:FaultTolerancePrimaryConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configPaths', 'instanceUuids', 'role', 'secondaries' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    