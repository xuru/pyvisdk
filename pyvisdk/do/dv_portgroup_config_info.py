# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVPortgroupConfigInfo(vim, *args, **kwargs):
    '''Configuration of a DistributedVirtualPortgroup.'''
    
    obj = vim.client.factory.create('ns0:DVPortgroupConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configVersion', 'defaultPortConfig', 'description',
        'distributedVirtualSwitch', 'key', 'name', 'numPorts', 'policy',
        'portNameFormat', 'scope', 'type', 'vendorSpecificConfig' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    