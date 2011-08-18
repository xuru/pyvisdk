# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmDiskFileQueryFilter(vim, *args, **kwargs):
    '''The filter for the virtual disk primary file.'''
    
    obj = vim.client.factory.create('ns0:VmDiskFileQueryFilter')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'controllerType', 'diskType', 'matchHardwareVersion', 'thin' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    