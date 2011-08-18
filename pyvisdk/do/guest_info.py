# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def GuestInfo(vim, *args, **kwargs):
    '''Information about the guest operating system.Most of this information is
    collected by VMware Tools. In general, be sure you have VMware Tools installed
    and that the virtual machine is running when you access this information.'''
    
    obj = vim.client.factory.create('ns0:GuestInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'appHeartbeatStatus', 'disk', 'guestFamily', 'guestFullName', 'guestId',
        'guestState', 'hostName', 'ipAddress', 'ipStack', 'net', 'screen',
        'toolsRunningStatus', 'toolsStatus', 'toolsVersion', 'toolsVersionStatus' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    