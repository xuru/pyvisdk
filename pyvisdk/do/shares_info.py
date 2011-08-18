# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def SharesInfo(vim, *args, **kwargs):
    '''Specification of shares.Shares are used to determine relative allocation
    between resource consumers. In general, a consumer with more shares gets
    proportionally more of the resource, subject to certain other constraints.'''
    
    obj = vim.client.factory.create('ns0:SharesInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'level', 'shares' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    