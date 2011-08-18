# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualVmxnetOption(vim, *args, **kwargs):
    '''The VirtualVmxnetOption data object type contains the options for the
    VirtualVmxnet data object type.'''
    
    obj = vim.client.factory.create('ns0:VirtualVmxnetOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type', 'macType', 'supportedOUI' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    