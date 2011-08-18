# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def UpdateVirtualMachineFilesResult(vim, *args, **kwargs):
    '''UpdateVirtualMachineFilesResult is the result returned to the
    UpdateVirtualMachineFiles_Task method.'''
    
    obj = vim.client.factory.create('ns0:UpdateVirtualMachineFilesResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'failedVmFile' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    