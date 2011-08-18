# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPCNet32Option(vim, *args, **kwargs):
    '''The VirtualPCNet32Option data object type defines the options for the
    VirtualPCNet32 data object type. Except for the boolean supportsMorphing
    option, the options are inherited from the VirtualEthernetCardOption data
    object type.'''
    
    obj = vim.client.factory.create('ns0:VirtualPCNet32Option')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type', 'macType', 'supportedOUI',
        'supportsMorphing' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    