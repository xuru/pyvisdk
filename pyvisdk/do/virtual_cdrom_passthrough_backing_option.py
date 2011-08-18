# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdromPassthroughBackingOption(vim, *args, **kwargs):
    '''The VirtualCdromOption.PassthroughBackingOption data object type contains the
    options for a pass-through CD-ROM device backing.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdromPassthroughBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable', 'exclusive' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    