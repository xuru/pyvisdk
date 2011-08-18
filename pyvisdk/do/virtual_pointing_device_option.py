# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPointingDeviceOption(vim, *args, **kwargs):
    '''The VirtualPointingDeviceOption data object type contains the options for the
    host mouse type defined in the VirtualPointingDevice data object type. These
    options include the valid selections for the mouse type, the supported mouse
    types, and the default mouse type.'''
    
    obj = vim.client.factory.create('ns0:VirtualPointingDeviceOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    