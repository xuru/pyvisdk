# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmwareDistributedVirtualSwitchVlanIdSpec(vim, *args, **kwargs):
    '''This data type defines the configuration when single vlanId is used for the
    port.'''
    
    obj = vim.client.factory.create('ns0:VmwareDistributedVirtualSwitchVlanIdSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'inherited', 'vlanId' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    