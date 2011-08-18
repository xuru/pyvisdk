# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFibreChannelTargetTransport(vim, *args, **kwargs):
    '''Fibre Channel transport information about a SCSI target.'''
    
    obj = vim.client.factory.create('ns0:HostFibreChannelTargetTransport')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'nodeWorldWideName', 'portWorldWideName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    