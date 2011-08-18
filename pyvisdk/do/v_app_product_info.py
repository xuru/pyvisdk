# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppProductInfo(vim, *args, **kwargs):
    '''Information that describes what product a vApp contains, e.g., what software
    that is installed in the contained virtual machines.'''
    
    obj = vim.client.factory.create('ns0:VAppProductInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'appUrl', 'classId', 'fullVersion', 'instanceId', 'key', 'name', 'productUrl',
        'vendor', 'vendorUrl', 'version' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    