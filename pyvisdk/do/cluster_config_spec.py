# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterConfigSpec(vim, *args, **kwargs):
    '''A complete cluster configuration. All fields are defined as optional. In case
    of a reconfiguration, unset fields are unchanged.'''
    
    obj = vim.client.factory.create('ns0:ClusterConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dasConfig', 'dasVmConfigSpec', 'drsConfig', 'drsVmConfigSpec', 'rulesSpec' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    