# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfProviderSummary(vim, *args, **kwargs):
    '''This data object type contains information about a performance provider, the
    type of statistics it generates, and the refreshRate for statistics generation.
    A performance provider is any managed object that generates real-time or
    historical statistics (or boththe currentSupported and summarySupported
    properties are not mutually exclusive).'''
    
    obj = vim.client.factory.create('ns0:PerfProviderSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'currentSupported', 'entity', 'refreshRate', 'summarySupported' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    