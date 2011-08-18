# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FaultToleranceSecondaryOpResult(vim, *args, **kwargs):
    '''FaultToleranceSecondaryOpResult is a data object that reports on the outcome of
    the CreateSecondaryVM_Task or EnableSecondaryVM_Task operation.'''
    
    obj = vim.client.factory.create('ns0:FaultToleranceSecondaryOpResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'powerOnAttempted', 'powerOnResult', 'vm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    