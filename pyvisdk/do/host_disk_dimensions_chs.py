# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskDimensionsChs(vim, *args, **kwargs):
    '''This data object type describes dimensions using the cylinder, head, sector
    (CHS) coordinate system. This coordinate system is generally needed for
    partitioning for legacy reasons. When defining partitions, many partitioning
    utilities do not function correctly when certain CHS constraints are not met.'''
    
    obj = vim.client.factory.create('ns0:HostDiskDimensionsChs')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cylinder', 'head', 'sector' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    