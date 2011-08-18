# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetCapabilities(vim, *args, **kwargs):
    '''Capability vector indicating the available product features.'''
    
    obj = vim.client.factory.create('ns0:HostNetCapabilities')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'canSetPhysicalNicLinkSpeed', 'dhcpOnVnicSupported', 'dnsConfigSupported',
        'ipRouteConfigSupported', 'ipV6Supported', 'maxPortGroupsPerVswitch',
        'nicTeamingPolicy', 'supportsNetworkHints', 'supportsNicTeaming',
        'supportsVlan', 'usesServiceConsoleNic', 'vnicConfigSupported',
        'vswitchConfigSupported' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    