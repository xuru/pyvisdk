# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSConfigInfo(vim, *args, **kwargs):
    '''Configuration of a DistributedVirtualSwitch.'''
    
    obj = vim.client.factory.create('ns0:DVSConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configVersion', 'contact', 'createTime', 'defaultPortConfig', 'description',
        'extensionKey', 'host', 'maxPorts', 'name', 'networkResourceManagementEnabled',
        'numPorts', 'numStandalonePorts', 'policy', 'productInfo', 'targetInfo',
        'uplinkPortgroup', 'uplinkPortPolicy', 'uuid', 'vendorSpecificConfig' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    