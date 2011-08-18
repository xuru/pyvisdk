# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaParamValue(vim, *args, **kwargs):
    '''Describes the the value of an iSCSI parameter, and whether the value is being
    inherited.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaParamValue')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'key', 'value', 'isInherited' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    