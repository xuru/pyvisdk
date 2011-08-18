# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourceAllocationInfo(vim, *args, **kwargs):
    '''The ResourceAllocationInfo data object specifies the reserved resource
    requirement as well as the limit (maximum allowed usage) for a given kind of
    resource. This is specified for both memory allocation (specified in MB) and
    CPU allocation (specified in MHz).For a ResourcePool, the
    ResourceAllocationInfo object describes both the guaranteed amount of the
    resource (reservation) and whether or not it is expandable
    (expandableReservation). If expandableReservation is true, then the resource
    pool can grow its reservation dynamically by borrowing unreserved resources
    from its parent resource pool. For the methods CreateResourcePool, CreateVApp
    and ImportVApp, you must provide values for all properties except
    overheadLimit; they are not optional. (Currently, overheadLimit is for VMware
    internal use only.)If the limit is configured, it must be greater than or equal
    to the reservation.'''
    
    obj = vim.client.factory.create('ns0:ResourceAllocationInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'expandableReservation', 'limit', 'overheadLimit', 'reservation', 'shares' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    