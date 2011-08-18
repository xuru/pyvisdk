# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfCompositeMetric(vim, *args, **kwargs):
    '''PerfCompositeMetric includes an optional aggregated entity performance
    statistics and a list of composite entities performance statistics. The
    aggregated entity statistics are optional because some entities, such as
    folders, do not have their own statistics.'''
    
    obj = vim.client.factory.create('ns0:PerfCompositeMetric')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'childEntity', 'entity' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    