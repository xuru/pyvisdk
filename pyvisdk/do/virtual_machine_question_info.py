# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineQuestionInfo(vim, *args, **kwargs):
    '''This data object type describes the question that is currently blocking a
    virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineQuestionInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'choice', 'id', 'message', 'text' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    