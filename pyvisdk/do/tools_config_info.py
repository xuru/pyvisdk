# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ToolsConfigInfo(vim, *args, **kwargs):
    '''ToolsConfigInfo is a data object type containing settings for the VMware Tools
    software running in the guest operating system.'''
    
    obj = vim.client.factory.create('ns0:ToolsConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'afterPowerOn', 'afterResume', 'beforeGuestReboot', 'beforeGuestShutdown',
        'beforeGuestStandby', 'pendingCustomization', 'syncTimeWithHost',
        'toolsUpgradePolicy', 'toolsVersion' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    