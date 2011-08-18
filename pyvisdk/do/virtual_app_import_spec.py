# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualAppImportSpec(vim, *args, **kwargs):
    '''A VAppImportSpec is used by ResourcePool.importVApp when importing vApps
    (single VM or multi-VM).It provides all information needed to import a
    VirtualApp.See also ImportSpec.'''
    
    obj = vim.client.factory.create('ns0:VirtualAppImportSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'entityConfig', 'child', 'name', 'resourcePoolSpec', 'vAppConfigSpec' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    