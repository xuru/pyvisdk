# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualController(vim, *args, **kwargs):
    '''VirtualController is the base data object type for a device controller in a
    virtual machine. VirtualController extends VirtualDevice to inherit general
    information about a controller (such as name and description), and to allow
    controllers to appear in a generic list of virtual devices.'''
    
    obj = vim.client.factory.create('ns0:VirtualController')
    
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
    