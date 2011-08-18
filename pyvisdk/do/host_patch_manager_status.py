# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPatchManagerStatus(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:HostPatchManagerStatus')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'applicable', 'id', 'installed', 'installState', 'integrity',
        'prerequisitePatch', 'reason', 'reconnectRequired', 'restartRequired',
        'supersededPatchIds', 'vmOffRequired' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    