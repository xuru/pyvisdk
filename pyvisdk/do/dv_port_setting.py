# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVPortSetting(vim, *args, **kwargs):
    '''Network related configuration of a DistributedVirtualPort.'''
    
    obj = vim.client.factory.create('ns0:DVPortSetting')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'blocked', 'inShapingPolicy', 'outShapingPolicy', 'vendorSpecificConfig',
        'vmDirectPathGen2Allowed' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    