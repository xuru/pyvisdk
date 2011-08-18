# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HttpNfcLeaseInfo(vim, *args, **kwargs):
    '''This class holds information about the lease, such as the entity covered by the
    lease, and HTTP URLs for up/downloading file backings.'''
    
    obj = vim.client.factory.create('ns0:HttpNfcLeaseInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceUrl', 'entity', 'hostMap', 'lease', 'leaseTimeout',
        'totalDiskCapacityInKB' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    