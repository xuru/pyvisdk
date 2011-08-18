# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConfigSummary(vim, *args, **kwargs):
    '''An overview of the key configuration parameters.'''
    
    obj = vim.client.factory.create('ns0:HostConfigSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'faultToleranceEnabled', 'featureVersion', 'name', 'port', 'product',
        'sslThumbprint', 'vmotionEnabled' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    