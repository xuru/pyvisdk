# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualPortgroupInfo(vim, *args, **kwargs):
    '''This class describes a DistributedVirtualPortgroup that a device backing can be
    attached to.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualPortgroupInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'portgroup', 'portgroupKey', 'portgroupName', 'portgroupType', 'switchName',
        'switchUuid', 'uplinkPortgroup' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    