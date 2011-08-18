# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareDVSConfigSpec(vim, *args, **kwargs):
    '''This class defines the VMware specific configuration for
    DistributedVirtualSwitch.'''
    
    obj = vim.client.factory.create('ns0:VMwareDVSConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configVersion', 'contact', 'defaultPortConfig', 'description', 'extensionKey',
        'host', 'maxPorts', 'name', 'numStandalonePorts', 'policy', 'uplinkPortgroup',
        'uplinkPortPolicy', 'vendorSpecificConfig', 'linkDiscoveryProtocolConfig',
        'maxMtu', 'pvlanConfigSpec' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    