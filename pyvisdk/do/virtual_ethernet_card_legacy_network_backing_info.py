# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualEthernetCardLegacyNetworkBackingInfo(vim, *args, **kwargs):
    '''The virtual Ethernet card legacy backing class.'''
    
    obj = vim.client.factory.create('ns0:VirtualEthernetCardLegacyNetworkBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    