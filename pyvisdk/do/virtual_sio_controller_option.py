# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSIOControllerOption(vim, *args, **kwargs):
    '''The VirtualSIOControllerOption data object type contains the options for a
    virtual Super IO Controller.'''
    
    obj = vim.client.factory.create('ns0:VirtualSIOControllerOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type', 'devices', 'supportedDevice',
        'numFloppyDrives', 'numParallelPorts', 'numSerialPorts' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    