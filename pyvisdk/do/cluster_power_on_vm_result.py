# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterPowerOnVmResult(vim, *args, **kwargs):
    '''PowerOnVmResult is the base class of the result returned to the
    PowerOnMultiVM_Task method.'''
    
    obj = vim.client.factory.create('ns0:ClusterPowerOnVmResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'attempted', 'notAttempted', 'recommendations' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    