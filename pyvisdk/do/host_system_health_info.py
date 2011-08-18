# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostSystemHealthInfo(vim, *args, **kwargs):
    '''This data object provides information about the health of the phyical system.
    The data is retrieved from numeric sensor probes.'''
    
    obj = vim.client.factory.create('ns0:HostSystemHealthInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'numericSensorInfo' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    