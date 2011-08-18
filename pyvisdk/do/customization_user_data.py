# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationUserData(vim, *args, **kwargs):
    '''Personal data pertaining to the owner of the virtual machine.The UserData data
    object type maps to the UserData key in the answer file. These values are
    transferred directly into the file that VirtualCenter stores on the target
    virtual disk. For more detailed information, see the document .'''
    
    obj = vim.client.factory.create('ns0:CustomizationUserData')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'computerName', 'fullName', 'orgName', 'productId' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    