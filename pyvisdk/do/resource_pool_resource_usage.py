# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourcePoolResourceUsage(vim, *args, **kwargs):
    '''Specifies the resource usage for either memory or CPU. For CPU the unit is MHz,
    for memory the unit is bytes.In the typical case, where a resourcepool is in a
    consistent state, unreservedForVm will be equal to unreservedForPool. Hence, we
    can simply say talk about unreserved resources.If the reservation on the
    resource pool is not expandable, then the following is true:If the reservation
    on the resource pool is expandable, then the following is true:'''
    
    obj = vim.client.factory.create('ns0:ResourcePoolResourceUsage')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'maxUsage', 'overallUsage', 'reservationUsed', 'reservationUsedForVm',
        'unreservedForPool', 'unreservedForVm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    