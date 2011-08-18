# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConsolePreferences(vim, *args, **kwargs):
    '''Preferences for the legacy console application that affect the way it behaves
    during power operations on the virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConsolePreferences')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'closeOnPowerOffOrSuspend', 'enterFullScreenOnPowerOn', 'powerOnWhenOpened' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    