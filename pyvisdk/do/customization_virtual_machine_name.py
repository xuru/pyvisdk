# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationVirtualMachineName(vim, *args, **kwargs):
    '''Specifies that VirtualCenter should generate a virtual machine name from a base
    prefix comprising the virtual machine entity name. A number is appended, if
    necessary, to make it unique.Virtual machine names are unique across the set of
    hosts and virtual machines known to the VirtualCenter instance. VMware Tools
    reports the names of existing virtual machines.'''
    
    obj = vim.client.factory.create('ns0:CustomizationVirtualMachineName')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [  ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    