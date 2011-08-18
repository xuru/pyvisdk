# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostProxySwitchSpec(vim, *args, **kwargs):
    '''This data object type describes the HostProxySwitch specification representing
    the properties on a HostProxySwitch that can be configured once the object
    exists.'''
    
    obj = vim.client.factory.create('ns0:HostProxySwitchSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backing' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    