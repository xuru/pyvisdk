# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationGuiRunOnce(vim, *args, **kwargs):
    '''The commands listed in the GuiRunOnce data object type are executed when a user
    logs on the first time after customization completes. The logon may be driven
    by the AutoLogon setting.The GuiRunOnce data object type maps to the GuiRunOnce
    key in the answer file. These values are transferred into the file that
    VirtualCenter stores on the target virtual disk. For more detailed information,
    see the document .'''
    
    obj = vim.client.factory.create('ns0:CustomizationGuiRunOnce')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'commandList' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    