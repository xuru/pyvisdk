# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ServiceConsoleReservationInfo(vim, *args, **kwargs):
    '''The ServiceConsoleReservationInfo data object type describes the amount of
    memory that is being reserved by the service console. Memory reserved for use
    by the service console is a hard reservation that cannot be changed except
    across hardware restarts.This memory that is reserved for the service console
    is used primarily to provide system management services. In addition, a small
    overhead is needed by each virtual machine on the service console.The only
    property of the data object that can be changed directly is the
    serviceConsoleReservedCfg property. This property indicates how much memory
    should be reserved for the service console on the next boot. In most cases,
    this amount is the same as the current reservation.'''
    
    obj = vim.client.factory.create('ns0:ServiceConsoleReservationInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'serviceConsoleReserved', 'serviceConsoleReservedCfg', 'unreserved' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    