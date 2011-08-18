# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostCpuPackage(vim, *args, **kwargs):
    '''Information about a physical CPU package.'''
    
    obj = vim.client.factory.create('ns0:HostCpuPackage')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'busHz', 'cpuFeature', 'description', 'hz', 'index', 'threadId', 'vendor' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    