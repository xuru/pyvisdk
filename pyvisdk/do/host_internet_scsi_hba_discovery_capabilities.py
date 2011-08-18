# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaDiscoveryCapabilities(vim, *args, **kwargs):
    '''The discovery capabilities for this host bus adapter. At least one discovery
    mode must always be active. Multiple modes may be active at the same time.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaDiscoveryCapabilities')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'iSnsDiscoverySettable', 'sendTargetsDiscoverySettable',
        'slpDiscoverySettable', 'staticTargetDiscoverySettable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    