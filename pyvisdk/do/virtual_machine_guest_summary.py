# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineGuestSummary(vim, *args, **kwargs):
    '''A subset of virtual machine guest information.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineGuestSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'guestFullName', 'guestId', 'hostName', 'ipAddress', 'toolsRunningStatus',
        'toolsStatus', 'toolsVersionStatus' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    