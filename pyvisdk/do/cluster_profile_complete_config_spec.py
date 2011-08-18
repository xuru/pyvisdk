# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterProfileCompleteConfigSpec(vim, *args, **kwargs):
    '''DataObject completely specifying the configuration of the profile.'''
    
    obj = vim.client.factory.create('ns0:ClusterProfileCompleteConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'annotation', 'enabled', 'name', 'complyProfile' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    