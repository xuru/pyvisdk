# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def SharesOption(vim, *args, **kwargs):
    '''Specification of shares.Object of this class specifies value ranges for object
    of instance SharesInfo'''
    
    obj = vim.client.factory.create('ns0:SharesOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'defaultLevel', 'sharesOption' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    