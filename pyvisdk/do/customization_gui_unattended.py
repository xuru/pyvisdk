# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationGuiUnattended(vim, *args, **kwargs):
    '''The GuiUnattended type maps to the GuiUnattended key in the answer file. These
    values are plugged directly into the file that VirtualCenter stores on the
    target virtual disk. For more detailed information, see the document'''
    
    obj = vim.client.factory.create('ns0:CustomizationGuiUnattended')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoLogon', 'autoLogonCount', 'password', 'timeZone' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    