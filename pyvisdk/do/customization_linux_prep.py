# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationLinuxPrep(vim, *args, **kwargs):
    '''This is the Linux counterpart to the Windows Sysprep object. LinuxPrep contains
    machine-wide settings that identify a Linux machine in the same way that the
    Sysprep type identifies a Windows machine.'''
    
    obj = vim.client.factory.create('ns0:CustomizationLinuxPrep')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'domain', 'hostName', 'hwClockUTC', 'timeZone' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    