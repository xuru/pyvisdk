# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationSysprepFailed(vim, *args, **kwargs):
    '''Sysprep failed to run in the guest during customization. This will most like
    have been caused by the fact that the wrong sysprep was used for the guest, so
    we include the version information in the event.'''
    
    obj = vim.client.factory.create('ns0:CustomizationSysprepFailed')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'template', 'logLocation', 'sysprepVersion', 'systemVersion' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    