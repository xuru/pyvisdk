# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualVmxnet2Option(vim, *args, **kwargs):
    '''The VirtualVmxnet2Option data object type contains the options for the
    VirtualVmxnet2 data object type.'''
    
    obj = vim.client.factory.create('ns0:VirtualVmxnet2Option')
    
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
    