# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineVideoCard(vim, *args, **kwargs):
    '''The VirtualVideoCard data object type represents a video card in a virtual
    machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineVideoCard')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'key', 'unitNumber',
        'enable3DSupport', 'numDisplays', 'useAutoDetect', 'videoRamSizeInKB' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    