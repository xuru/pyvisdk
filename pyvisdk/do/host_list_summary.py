# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostListSummary(vim, *args, **kwargs):
    '''This data object type encapsulates a typical set of host information that is
    useful for list views and summary pages.VirtualCenter can retrieve this
    information very efficiently, even for a large set of hosts.'''
    
    obj = vim.client.factory.create('ns0:HostListSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'config', 'currentEVCModeKey', 'customValue', 'hardware', 'host',
        'managementServerIp', 'maxEVCModeKey', 'overallStatus', 'quickStats',
        'rebootRequired', 'runtime' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    