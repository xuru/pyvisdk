# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CheckResult(vim, *args, **kwargs):
    '''The result of a call to any of the methods in either
    VirtualMachineCompatibilityChecker or VirtualMachineProvisioningChecker.'''
    
    obj = vim.client.factory.create('ns0:CheckResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'error', 'host', 'vm', 'warning' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    