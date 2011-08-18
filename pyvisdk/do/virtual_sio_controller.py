# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSIOController(vim, *args, **kwargs):
    '''This data object type defines a Super IO Controller for floppy drives, parallel
    ports, and serial ports.'''
    
    obj = vim.client.factory.create('ns0:VirtualSIOController')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'key', 'unitNumber',
        'busNumber', 'device' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    