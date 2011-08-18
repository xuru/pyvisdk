# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceConfigSpec(vim, *args, **kwargs):
    '''The VirtualDeviceSpec data object type encapsulates change specifications for
    an individual virtual device. The virtual device being added or modified must
    be fully specified.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'device', 'fileOperation', 'operation' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    