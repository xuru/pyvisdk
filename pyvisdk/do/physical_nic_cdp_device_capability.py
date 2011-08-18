# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNicCdpDeviceCapability(vim, *args, **kwargs):
    '''The capability of the CDP-awared device that connects to a PNIC.
    PhysicalNicCdpInfo'''
    
    obj = vim.client.factory.create('ns0:PhysicalNicCdpDeviceCapability')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'host', 'igmpEnabled', 'networkSwitch', 'repeater', 'router',
        'sourceRouteBridge', 'transparentBridge' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    