# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPS2ControllerOption(vim, *args, **kwargs):
    '''The VirtualPS2ControllerOption data object type contains the options for a
    virtual PS/2 controller for keyboards and mice. In addition to the options
    defined in the VirtualControllerOption data object type, these options include
    the number of keyboards and mice.'''
    
    obj = vim.client.factory.create('ns0:VirtualPS2ControllerOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type', 'devices', 'supportedDevice',
        'numKeyboards', 'numPointingDevices' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    