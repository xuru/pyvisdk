# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHardwareStatusInfo(vim, *args, **kwargs):
    '''Data object representing the status of the hardware components of the host.'''
    
    obj = vim.client.factory.create('ns0:HostHardwareStatusInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cpuStatusInfo', 'memoryStatusInfo', 'storageStatusInfo' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    