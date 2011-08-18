# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterProfileConfigServiceCreateSpec(vim, *args, **kwargs):
    '''DataObject which allows reconfiguration of a profile based on services that
    will be available on the cluster.'''
    
    obj = vim.client.factory.create('ns0:ClusterProfileConfigServiceCreateSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'annotation', 'enabled', 'name', 'serviceType' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    