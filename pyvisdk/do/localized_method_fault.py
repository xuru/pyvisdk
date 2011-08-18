# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def LocalizedMethodFault(vim, *args, **kwargs):
    '''A wrapper class used to pass MethodFault data objects over the wire along with
    a localized display message for the fault.'''
    
    obj = vim.client.factory.create('ns0:LocalizedMethodFault')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'fault', 'localizedMessage' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    