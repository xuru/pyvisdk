# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfManagerCommonParams(vim, *args, **kwargs):
    '''A common super-class for basic OVF descriptor parameters'''
    
    obj = vim.client.factory.create('ns0:OvfManagerCommonParams')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deploymentOption', 'locale', 'msgBundle' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    