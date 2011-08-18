# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHba(vim, *args, **kwargs):
    '''This data object type describes the iSCSI host bus adapter interface.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHba')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bus', 'device', 'driver', 'key', 'model', 'pci', 'status', 'advancedOptions',
        'authenticationCapabilities', 'authenticationProperties',
        'configuredSendTarget', 'configuredStaticTarget', 'currentSpeedMb',
        'digestCapabilities', 'digestProperties', 'discoveryCapabilities',
        'discoveryProperties', 'ipCapabilities', 'ipProperties', 'iScsiAlias',
        'iScsiName', 'isSoftwareBased', 'maxSpeedMb', 'supportedAdvancedOptions' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    