# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPatchManagerStatusPrerequisitePatch(vim, *args, **kwargs):
    '''Updates that are required to be installed before this update can be installed
    on the server. In addition to being installed on the server, an update can have
    additional requirement on the server or services running on the server
    pertaining to the prerequisite update.'''
    
    obj = vim.client.factory.create('ns0:HostPatchManagerStatusPrerequisitePatch')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'id', 'installState' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    