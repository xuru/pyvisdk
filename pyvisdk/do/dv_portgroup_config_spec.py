# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVPortgroupConfigSpec(vim, *args, **kwargs):
    '''Specification to reconfigure a DistributedVirtualPortgroup.'''
    
    obj = vim.client.factory.create('ns0:DVPortgroupConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configVersion', 'defaultPortConfig', 'description', 'name', 'numPorts',
        'policy', 'portNameFormat', 'scope', 'type', 'vendorSpecificConfig' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    